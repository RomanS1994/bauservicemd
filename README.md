# BauServiceMD

Static multilingual website for the independent renovation craftsman Dmytro Mykhavkiv, serving Frankfurt am Main and the surrounding area.

Built with semantic HTML, separate CSS files and a small progressively enhanced JavaScript file. No database, trackers, third-party fonts or embedded maps.

## Languages

- Ukrainian: `uk/`
- German: `de/`
- English: `en/`

## Update pages

Run `python3 build.py` to regenerate the committed HTML pages. Edit the generator for shared layouts and translations; edit `assets/css/` for styling. GitHub Pages publishes the root of `main` directly; no framework or package installation is needed.

## Contact form

The form submits to FormSubmit using a JSON POST after explicit submission, without opening an email client. The browser sends no cookies with the AJAX request and stores no entries persistently. A honeypot, validation, request timeout and duplicate-submit guard are included. Errors retain entries; only an accepted response clears unchanged fields. Direct WhatsApp, telephone and email links remain available.

**Activation required:** The owner of `renovierungsservicedima@gmail.com` must activate the form using the FormSubmit confirmation email triggered by the first submission. Check Spam as well. Until activation and a real delivery check are complete, email delivery is unverified. After connecting a different domain or changing the destination address, verify activation and delivery again.

No API secrets are used. Provider documentation: https://formsubmit.co/documentation and https://formsubmit.co/help. The privacy pages disclose the external processor and its documented 30-day submission archive. Owner review of provider terms and the final legal wording remains necessary.

## Content

The photographs are generated design assets, not verified photographs of completed client commissions. Replace them with owner-approved project photographs when available. The legal pages clearly identify missing owner information and need owner review before use as final legal notices.

Business contact: +49 1577 8582592 · renovierungsservicedima@gmail.com
