#!/usr/bin/env python3
"""Static, offline guardrails for the isolated commercial showcase."""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
PAGES=[ROOT/"index.html",*[ROOT/x/"index.html" for x in ("saas","ecommerce","servicios")]]

class Audit(HTMLParser):
    def __init__(self):
        super().__init__();self.tags=[];self.attrs=[];self.form_count=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);self.tags.append(tag);self.attrs.append((tag,a))
        if tag=="form":self.form_count+=1

def audit(path):
    text=path.read_text(encoding="utf-8")
    p=Audit();p.feed(text)
    errors=[]
    for tag in ("html","head","title","main","h1","footer"):
        if tag not in p.tags:errors.append("missing "+tag)
    if '<meta name="viewport"' not in text:errors.append("missing responsive viewport")
    if 'fictici' not in text.lower() and 'sintétic' not in text.lower():
        errors.append("missing demo disclosure")
    for tag,a in p.attrs:
        if tag=="html" and a.get("lang")!="es-MX":errors.append("incorrect language")
        if tag=="script" and a.get("src"):errors.append("external script")
        if tag=="form" and (a.get("action") or a.get("method","").lower()=="post"):
            errors.append("form network submission")
        if tag=="img" and "alt" not in a:errors.append("missing image alt")
        if tag=="a" and a.get("href","").startswith(("https:","http:")):
            errors.append("external navigation must be reviewed")
        if tag=="link" and a.get("rel")=="stylesheet":
            if not (path.parent/a.get("href","")).resolve().is_file():
                errors.append("missing stylesheet")
    if p.form_count:
        if "preventDefault()" not in text or "reportValidity()" not in text:
            errors.append("demo forms must prevent network submission and validate")
        if 'role="status"' not in text:errors.append("missing accessible confirmation")
    return errors

def main():
    failed=False
    for page in PAGES:
        if not page.is_file():
            print("FAIL missing "+str(page));failed=True;continue
        issues=audit(page)
        print(("FAIL" if issues else "PASS")+" "+str(page.relative_to(ROOT))+
              (": "+", ".join(issues) if issues else ""))
        failed=failed or bool(issues)
    return 1 if failed else 0
if __name__=="__main__":sys.exit(main())
