#!/usr/bin/env python3
"""Build the plain-HTML BauServiceMD website. No third-party dependencies."""
from pathlib import Path
from html import escape as esc
from privacy_content import POLICY, TITLES

ROOT = Path(__file__).resolve().parent
BASE = 'https://romans1994.github.io/bauservicemd'
PHONE = '+49 1577 8582592'
EMAIL = 'renovierungsservicedima@gmail.com'
WA = 'https://wa.me/4915778582592'

COPY = {
 'uk': {
  'lang_name': 'Українська', 'nav': ['Послуги', 'Роботи', 'Про мене', 'Контакти'], 'connect': 'Зв’язатися', 'menu': 'Меню', 'skip': 'Перейти до змісту', 'home': 'Головна', 'region': 'Франкфурт-на-Майні та околиці', 'private': 'Приватний майстер',
  'hero_title': 'Ремонт та<br>оздоблення житла.', 'hero_description': 'Від окремого завдання до оновлення кімнати. Обговоримо, що потрібно саме вам.', 'hero_cta': 'Обговорити ремонт', 'view_work': 'Переглянути роботи', 'hero_alt': 'Ілюстрація світлої кімнати з дерев’яною підлогою після оновлення', 'illustration': 'Ілюстративне зображення', 'image_notice': 'Фотографії на сайті — ілюстрації, а не портфоліо виконаних замовлень.',
  'services_label': 'Послуги', 'services_title': 'З чим можу<br>допомогти?', 'services_intro': 'Кожне житло й кожне завдання різні. Почнемо з того, що ви хочете змінити.', 'services_note': 'Конкретний склад і можливість виконання робіт уточнюються під час розмови.', 'all_services': 'Усі послуги', 'details': 'Детальніше',
  'services': [
   ['Ремонт та внутрішні роботи', 'Оновлення кімнати чи окремої частини житла. Спочатку обговоримо стан приміщення та потрібний результат.', ['Огляд вашого завдання за описом і фото', 'Уточнення потрібних підготовчих та оздоблювальних робіт', 'Погодження матеріалів і послідовності виконання']],
   ['Укладання ламінату та підлогових покриттів', 'Укладання ламінату й відповідних підлогових покриттів, включно з підготовчими та завершальними роботами.', ['Уточнення стану основи та обраного покриття', 'Обговорення підкладки, переходів і плінтусів', 'Погодження обсягу укладання та завершальних деталей']],
   ['Монтаж і демонтаж', 'Допомога з установленням або зняттям окремих елементів та підготовкою приміщення до наступних робіт.', ['Уточнення того, що потрібно встановити чи зняти', 'Обговорення матеріалів, кріплень і доступу', 'Погодження підготовки приміщення та завершення робіт']],
   ['Дрібний ремонт і догляд за житлом', 'Невеликі побутові завдання та господарські роботи. Невеликі замовлення теж можна обговорити.', ['Фото або короткий опис несправності чи завдання', 'Уточнення можливості виконання та потрібних матеріалів', 'Погодження зручного часу та доступу до приміщення']]
  ],
  'work_label': 'Роботи', 'work_title': 'Роботи — у деталях.', 'work_intro': 'Поки готую фотографії реальних об’єктів, тут можна переглянути приклади оформлення інтер’єру.', 'all_work': 'Переглянути приклади', 'example_title': 'Світлий простір і природні матеріали', 'example_detail': 'Оздоблення та стики зблизька', 'example_wide': 'Загальний вигляд кімнати', 'example_tag': 'Демонстраційне зображення', 'example_link': 'Про цей приклад',
  'about_label': 'Про майстра', 'about_title': 'Спілкування<br>напряму.', 'about_short': 'Мене звати Dmytro Mykhavkiv. Я займаюся ремонтом, внутрішнім облаштуванням та монтажними роботами у Франкфурті-на-Майні та околицях.', 'about_more': 'Більше про мене', 'about_paragraphs': ['Перший практичний досвід у ремонтних роботах я отримав у 2013 році. Відтоді брав участь у різних проєктах і поступово розвивав свої ремісничі навички.', 'Понад п’ять років практичного досвіду я здобув у Німеччині. У своїй роботі приділяю увагу акуратному виконанню, надійності та зрозумілим домовленостям.', 'Невеликий ремонт, монтаж або оновлення кімнати — спочатку я хочу зрозуміти ваше завдання. Після цього чесно скажу, чи можу допомогти, та обговорю з вами наступні кроки.'],
  'process_label': 'Порядок співпраці', 'process_title': 'Як домовитися про роботу.', 'process_note': 'Деталі та порядок узгоджуються для вашого завдання.', 'steps': [['Звернення', 'Напишіть, зателефонуйте або надішліть кілька фотографій.'], ['Уточнення деталей', 'Обговоримо побажання, умови на об’єкті та потрібний результат.'], ['Узгодження обсягу', 'Домовимося про роботи, матеріали та наступні кроки.'], ['Виконання та здача', 'Після погодження переходжу до роботи й обговорюю з вами результат.']],
  'prepare_label': 'Що підготувати', 'prepare_title': 'Що підготувати<br>для першої розмови?', 'preparations': [['Фото приміщення', 'Кілька актуальних фото кімнати або зони, де потрібні роботи.'], ['Короткий опис завдання', 'Що саме потрібно змінити та які побажання є до результату.'], ['Бажаний час початку', 'Орієнтовний період, коли вам було б зручно почати.']],
  'faq_label': 'Питання та відповіді', 'faq_title': 'Поширені запитання.', 'faq': [['Чи можна почати з фотографій?', 'Так. Короткий опис і кілька фотографій допоможуть скласти перше уявлення про завдання. За потреби деталі уточнимо під час розмови.'], ['Як обговорити матеріали?', 'Розкажіть, які матеріали вже є або який результат ви хочете отримати. До початку робіт узгодимо потрібні матеріали та хто їх готує.'], ['Як узгодити обсяг робіт?', 'Спочатку обговоримо ваше завдання та умови на об’єкті. Далі визначимо конкретний перелік робіт і наступні кроки.'], ['Де ви працюєте?', 'У Франкфурті-на-Майні та околицях. Напишіть місце розташування об’єкта, щоб уточнити можливість виїзду.']],
  'contact_label': 'Контакти', 'contact_title': 'Що плануєте<br>оновити?', 'contact_intro': 'Можна почати з кількох слів або фото. Я розгляну ваше звернення й чесно скажу, чи зможу допомогти.', 'call': 'Зателефонувати', 'write': 'Написати email', 'form_title': 'Підготуйте лист', 'name': 'Ім’я', 'contact': 'Телефон або email', 'message': 'Що потрібно зробити?', 'name_placeholder': 'Як до вас звертатися', 'contact_placeholder': 'Контакт для відповіді', 'message_placeholder': 'Коротко опишіть завдання, приміщення та побажання', 'submit': 'Відкрити чернетку листа', 'form_note': 'Форма відкриє вашу поштову програму. Лист потрібно надіслати в ній; сайт не надсилає заявку автоматично.', 'form_status': 'Якщо поштова програма не відкрилася, напишіть безпосередньо на email або у WhatsApp.', 'privacy_link': 'Про обробку даних', 'subject': 'Звернення із сайту BauServiceMD', 'required': 'обов’язкове поле', 'phone_label': 'Телефон і WhatsApp', 'email_label': 'Електронна пошта',
  'footer_line': 'Ремонт та монтаж. Особистий підхід до вашого завдання.', 'legal_notice': 'Юридична інформація ще доповнюється власником. Ця версія сайту є попереднім переглядом.', 'impressum_title': 'Impressum', 'privacy_title': 'Конфіденційність', 'legal_intro': 'Відомості про відповідального за сайт', 'address': 'Адреса', 'owner': 'Власник', 'pending': 'Додаткові обов’язкові реквізити, якщо вони застосовні, та фінальну редакцію має надати власник. Невідомі реєстраційні й податкові номери не додані.', 'privacy_intro': 'Інформація про обробку персональних даних під час відвідування сайту та звернення до майстра.', 'privacy_paragraphs': ['Відповідальний за сайт: Renovierungsservice Dmytro Mykhavkiv, Dmytro Mykhavkiv, Ringelstraße 54, 60385 Frankfurt am Main. Зв’язок: renovierungsservicedima@gmail.com.', 'Цей статичний сайт розміщено на GitHub Pages. Під час відкриття сторінок запити обробляє хостинг-провайдер. Інформацію про його обробку даних наведено в політиці конфіденційності GitHub.', 'У цій версії немає аналітики, рекламних трекерів, вбудованих карт або зовнішніх вебшрифтів. Сайт не встановлює власних cookies та не зберігає поля форми на сервері.', 'Поля форми обробляються у вашому браузері для створення чернетки у вашій поштовій програмі. Надсилання відбувається лише після вашої дії у поштовій програмі. Посилання WhatsApp відкриває сторонній сервіс; телефонне посилання — програму для дзвінків.', 'Це фактична технічна інформація, а не завершена Datenschutzerklärung. Повний юридичний текст щодо обробки звернень, строків зберігання та прав відвідувача має надати власник перед комерційним запуском.'], 'github_policy': 'Політика конфіденційності GitHub',
  'service_scope': 'Що можна обговорити', 'service_caveat': 'Кожне завдання оцінюється окремо. Цей опис не включає електромонтажні, сантехнічні чи конструктивні роботи, що потребують окремої кваліфікації.', 'back_services': 'До всіх послуг', 'example_heading': 'Ілюстративний приклад інтер’єру', 'example_intro': 'Ця сторінка показує лише напрям оформлення. Зображення створені для дизайну сайту й не є фотографіями виконаного мною замовлення.', 'example_body': 'Світлі поверхні, дерев’яне покриття та акуратні переходи між матеріалами допомагають пояснити побажання до приміщення. Надішліть власні фото й розкажіть, що саме хочете оновити — обсяг можливих робіт обговоримо окремо.', 'back_work': 'До прикладів', 'contact_page_title': 'Розкажіть, що ви плануєте.', 'about_page_title': 'Ремонт — це ще й<br>зрозумілі домовленості.', 'services_page_title': 'Мої послуги.', 'projects_page_title': 'Простір, матеріали<br>та деталі.',
 },
 'de': {
  'lang_name': 'Deutsch', 'nav': ['Leistungen', 'Einblicke', 'Über mich', 'Kontakt'], 'connect': 'Kontakt aufnehmen', 'menu': 'Menü', 'skip': 'Zum Inhalt springen', 'home': 'Startseite', 'region': 'Frankfurt am Main und Umgebung', 'private': 'Selbstständiger Handwerker',
  'hero_title': 'Renovierung und<br>Innenausbau.', 'hero_description': 'Von einer einzelnen Aufgabe bis zur Erneuerung eines Raumes. Besprechen wir, was Sie vorhaben.', 'hero_cta': 'Renovierung besprechen', 'view_work': 'Einblicke ansehen', 'hero_alt': 'Illustration eines hellen renovierten Wohnraums mit Holzfußboden', 'illustration': 'Illustrative Abbildung', 'image_notice': 'Die Bilder auf dieser Website sind Illustrationen und keine Referenzen ausgeführter Kundenaufträge.',
  'services_label': 'Leistungen', 'services_title': 'Was kann ich<br>für Sie tun?', 'services_intro': 'Jede Wohnung ist anders, und nicht jede Aufgabe passt in eine feste Liste. Zuerst möchte ich verstehen, was Sie sich wünschen.', 'services_note': 'Der konkrete Leistungsumfang und die mögliche Ausführung werden im persönlichen Gespräch geklärt.', 'all_services': 'Alle Leistungen', 'details': 'Mehr erfahren',
  'services': [
   ['Renovierung und Innenausbau', 'Einen Raum auffrischen oder einen einzelnen Bereich verändern. Wir besprechen zunächst den Zustand und das gewünschte Ergebnis.', ['Ihre Aufgabe anhand von Beschreibung und Fotos kennenlernen', 'Erforderliche Vorbereitungs- und Ausbauarbeiten klären', 'Materialien und Reihenfolge der Arbeiten besprechen']],
   ['Laminat- und Bodenverlegung', 'Verlegung von Laminat und geeigneten Bodenbelägen sowie die dazugehörigen Vorbereitungs- und Abschlussarbeiten.', ['Zustand des Untergrunds und gewünschten Belag klären', 'Unterlage, Übergänge und Sockelleisten besprechen', 'Verlegeumfang und abschließende Details vereinbaren']],
   ['Montage und Demontage', 'Verschiedene Montage- und Demontagearbeiten sowie die Vorbereitung von Räumen für die nächsten Arbeitsschritte.', ['Klären, was montiert oder entfernt werden soll', 'Materialien, Befestigungen und Zugang besprechen', 'Vorbereitung und Abschluss der Arbeiten vereinbaren']],
   ['Kleinreparaturen und Hausmeisterservice', 'Kleinere Aufgaben und praktische Hilfe rund um Ihre Wohnung. Auch kleine Aufträge können wir gerne besprechen.', ['Fotos oder eine kurze Beschreibung der Aufgabe', 'Mögliche Ausführung und benötigte Materialien klären', 'Passenden Zeitpunkt und Zugang zur Wohnung vereinbaren']]
  ],
  'work_label': 'Einblicke', 'work_title': 'Räume und ihre Details.', 'work_intro': 'Während die Fotos realer Projekte vorbereitet werden, finden Sie hier Gestaltungsbeispiele für Innenräume.', 'all_work': 'Alle Beispiele ansehen', 'example_title': 'Helle Räume und natürliche Materialien', 'example_detail': 'Oberflächen und Übergänge im Detail', 'example_wide': 'Ein Blick auf den gesamten Raum', 'example_tag': 'Illustratives Gestaltungsbeispiel', 'example_link': 'Über dieses Beispiel',
  'about_label': 'Über mich', 'about_title': 'Direkt miteinander<br>sprechen.', 'about_short': 'Mein Name ist Dmytro Mykhavkiv. Ich bin im Bereich Renovierung, Innenausbau und Montageservice in Frankfurt am Main und Umgebung tätig.', 'about_more': 'Mehr über mich', 'about_paragraphs': ['Meine ersten praktischen Erfahrungen im Renovierungsbereich habe ich 2013 gesammelt. Seitdem war ich an unterschiedlichen Projekten beteiligt und konnte meine handwerklichen Fähigkeiten kontinuierlich weiterentwickeln.', 'Mehr als fünf Jahre praktische Berufserfahrung habe ich in Deutschland gesammelt. Bei meiner Arbeit lege ich Wert auf sorgfältige Ausführung, Zuverlässigkeit und klare Absprachen.', 'Ob kleine Reparaturen, Montagearbeiten oder die Erneuerung eines Raumes: Zuerst möchte ich Ihre Aufgabe verstehen. Anschließend sage ich Ihnen offen, ob ich helfen kann, und wir besprechen die nächsten Schritte.'],
  'process_label': 'Zusammenarbeit', 'process_title': 'So besprechen wir Ihre Aufgabe.', 'process_note': 'Die einzelnen Schritte werden passend zu Ihrer Aufgabe vereinbart.', 'steps': [['Kontakt', 'Schreiben Sie mir, rufen Sie an oder schicken Sie einige Fotos.'], ['Details klären', 'Wir besprechen Ihre Wünsche, die Bedingungen vor Ort und das Ziel.'], ['Umfang vereinbaren', 'Wir stimmen Arbeiten, Materialien und nächste Schritte ab.'], ['Ausführung und Übergabe', 'Nach der Abstimmung führe ich die Arbeiten aus und bespreche mit Ihnen das Ergebnis.']],
  'prepare_label': 'Vorbereitung', 'prepare_title': 'Was hilft beim<br>ersten Gespräch?', 'preparations': [['Fotos des Raumes', 'Einige aktuelle Aufnahmen des Raumes oder des betroffenen Bereichs.'], ['Eine kurze Beschreibung', 'Was soll verändert werden und welches Ergebnis wünschen Sie sich?'], ['Gewünschter Beginn', 'Der ungefähre Zeitraum, in dem Sie die Arbeiten beginnen möchten.']],
  'faq_label': 'Fragen und Antworten', 'faq_title': 'Häufige Fragen.', 'faq': [['Kann ich zunächst Fotos schicken?', 'Ja. Eine kurze Beschreibung und einige Fotos helfen mir, einen ersten Eindruck zu gewinnen. Weitere Einzelheiten klären wir bei Bedarf im Gespräch.'], ['Wie werden Materialien besprochen?', 'Teilen Sie mir mit, welche Materialien bereits vorhanden sind oder welches Ergebnis Sie wünschen. Vor Beginn stimmen wir ab, was benötigt wird und wer es bereitstellt.'], ['Wie wird der Arbeitsumfang vereinbart?', 'Zuerst besprechen wir Ihre Aufgabe und die Bedingungen vor Ort. Anschließend klären wir den konkreten Umfang und die nächsten Schritte.'], ['Wo sind Sie tätig?', 'In Frankfurt am Main und Umgebung. Nennen Sie mir den Standort des Objekts, damit wir die Anfahrt klären können.']],
  'contact_label': 'Kontakt', 'contact_title': 'Was möchten Sie<br>verändern?', 'contact_intro': 'Oft reichen ein paar Worte oder Fotos für einen ersten Eindruck. Ich schaue mir Ihre Anfrage an und sage offen, ob ich helfen kann.', 'call': 'Anrufen', 'write': 'E-Mail schreiben', 'form_title': 'E-Mail vorbereiten', 'name': 'Name', 'contact': 'Telefon oder E-Mail', 'message': 'Was möchten Sie machen lassen?', 'name_placeholder': 'Wie darf ich Sie ansprechen?', 'contact_placeholder': 'Kontakt für die Rückmeldung', 'message_placeholder': 'Beschreiben Sie kurz Ihre Aufgabe, den Raum und Ihre Wünsche', 'submit': 'E-Mail-Entwurf öffnen', 'form_note': 'Das Formular öffnet Ihr E-Mail-Programm. Sie senden die Nachricht dort selbst ab; die Website verschickt keine Anfrage automatisch.', 'form_status': 'Falls sich kein E-Mail-Programm öffnet, schreiben Sie bitte direkt per E-Mail oder WhatsApp.', 'privacy_link': 'Informationen zur Datenverarbeitung', 'subject': 'Anfrage über BauServiceMD', 'required': 'Pflichtfeld', 'phone_label': 'Telefon und WhatsApp', 'email_label': 'E-Mail',
  'footer_line': 'Renovierung und Montage. Persönliche Beratung zu Ihrem Vorhaben.', 'legal_notice': 'Die rechtlichen Angaben werden vom Inhaber noch vervollständigt. Diese Website ist eine Vorschau.', 'impressum_title': 'Impressum', 'privacy_title': 'Datenschutzerklärung', 'legal_intro': 'Angaben zum Verantwortlichen dieser Website', 'address': 'Anschrift', 'owner': 'Inhaber', 'pending': 'Weitere erforderliche Angaben, soweit anwendbar, und die abschließende Fassung sind vom Inhaber bereitzustellen. Nicht vorliegende Register- oder Steuernummern wurden nicht ergänzt.', 'privacy_intro': 'Informationen zur Verarbeitung personenbezogener Daten beim Besuch dieser Website und bei einer Kontaktaufnahme.', 'privacy_paragraphs': ['Verantwortlich für diese Website: Renovierungsservice Dmytro Mykhavkiv, Dmytro Mykhavkiv, Ringelstraße 54, 60385 Frankfurt am Main. Kontakt: renovierungsservicedima@gmail.com.', 'Diese statische Website wird auf GitHub Pages bereitgestellt. Beim Seitenaufruf verarbeitet der Hostinganbieter die Anfragen. Angaben hierzu finden Sie in der Datenschutzerklärung von GitHub.', 'Diese Version verwendet keine Analysewerkzeuge, Werbetracker, eingebetteten Karten oder extern geladenen Webfonts. Die Website setzt keine eigenen Cookies und speichert Formulareingaben nicht auf einem Server.', 'Die Formulareingaben werden in Ihrem Browser genutzt, um einen Entwurf in Ihrem E-Mail-Programm zu erstellen. Sie versenden die Nachricht erst durch Ihre eigene Aktion im E-Mail-Programm. WhatsApp-Links öffnen einen externen Dienst; Telefonlinks öffnen Ihre Telefonanwendung.', 'Dies ist eine technische Beschreibung und keine abschließende Datenschutzerklärung. Der Inhaber muss vor dem kommerziellen Start den vollständigen Text unter anderem zur Bearbeitung von Anfragen, Speicherdauer und zu den Rechten der Besucher bereitstellen.'], 'github_policy': 'GitHub-Datenschutzerklärung',
  'service_scope': 'Das können wir besprechen', 'service_caveat': 'Jede Aufgabe wird einzeln geprüft. Diese Beschreibung umfasst keine Elektro-, Sanitär- oder statisch relevanten Arbeiten, für die eine gesonderte Qualifikation erforderlich ist.', 'back_services': 'Zu allen Leistungen', 'example_heading': 'Ein illustratives Gestaltungsbeispiel', 'example_intro': 'Diese Seite zeigt ausschließlich eine gestalterische Richtung. Die Bilder wurden für das Webdesign erstellt und zeigen keinen von mir ausgeführten Kundenauftrag.', 'example_body': 'Helle Flächen, Holzbeläge und sorgfältige Materialübergänge können helfen, Ihre Vorstellungen zu erklären. Senden Sie eigene Fotos und beschreiben Sie, was Sie verändern möchten. Den möglichen Arbeitsumfang besprechen wir individuell.', 'back_work': 'Zurück zu den Beispielen', 'contact_page_title': 'Erzählen Sie mir, was Sie vorhaben.', 'about_page_title': 'Handwerk und<br>klare Absprachen.', 'services_page_title': 'Meine Leistungen.', 'projects_page_title': 'Räume, Materialien<br>und Details.',
 },
 'en': {
  'lang_name': 'English', 'nav': ['Services', 'Work', 'About me', 'Contact'], 'connect': 'Get in touch', 'menu': 'Menu', 'skip': 'Skip to content', 'home': 'Home', 'region': 'Frankfurt am Main and surrounding areas', 'private': 'Independent tradesperson',
  'hero_title': 'Renovation and<br>interior finishing.', 'hero_description': 'From a small repair to a room update. Let’s discuss what you have in mind.', 'hero_cta': 'Discuss your renovation', 'view_work': 'Explore the gallery', 'hero_alt': 'Illustration of a bright renovated living room with a wooden floor', 'illustration': 'Illustrative image', 'image_notice': 'The images on this website are illustrations, not a portfolio of completed customer projects.',
  'services_label': 'Services', 'services_title': 'How can<br>I help?', 'services_intro': 'Every home is different, and not every task fits a fixed list. First, I want to understand what you would like to change.', 'services_note': 'I will discuss the scope with you and let you know whether I can take on the work.', 'all_services': 'All services', 'details': 'Find out more',
  'services': [
   ['Renovation and interior work', 'Refresh a room or update one part of your home. We start by discussing its condition and your intended result.', ['Review your task using a description and photos', 'Clarify the preparation and finishing work needed', 'Discuss materials and the order of work']],
   ['Laminate and flooring installation', 'Installation of laminate and suitable floor coverings, including associated preparation and finishing work.', ['Clarify the condition of the subfloor and chosen covering', 'Discuss underlay, transitions and skirting boards', 'Agree the installation scope and finishing details']],
   ['Assembly and dismantling', 'Help with assembling or removing individual items and preparing rooms for the next stage of work.', ['Clarify what needs to be assembled or removed', 'Discuss materials, fixings and access', 'Agree preparation and completion of the task']],
   ['Small repairs and property care', 'Small repairs and practical help around your home. You are welcome to get in touch about smaller jobs too.', ['Photos or a short description of the problem or task', 'Clarify what is possible and which materials are needed', 'Agree a suitable time and access to the property']]
  ],
  'work_label': 'Work', 'work_title': 'Spaces and their details', 'work_intro': 'While photos of actual projects are being prepared, you can explore these illustrative interior examples.', 'all_work': 'View all examples', 'example_title': 'Bright spaces and natural materials', 'example_detail': 'Finishes and transitions up close', 'example_wide': 'A view of the whole room', 'example_tag': 'Illustrative design example', 'example_link': 'About this example',
  'about_label': 'About me', 'about_title': 'A direct<br>conversation.', 'about_short': 'My name is Dmytro Mykhavkiv. I provide renovation, interior finishing and assembly services in Frankfurt am Main and the surrounding areas.', 'about_more': 'More about me', 'about_paragraphs': ['I gained my first practical renovation experience in 2013. Since then, I have taken part in a range of projects and continued to develop my practical skills.', 'I have gained more than five years of practical work experience in Germany. I value careful workmanship, reliability and clear agreements with customers.', 'Whether you need a small repair, assembly work or a room update, I first want to understand the task. I will then tell you openly whether I can help, and we can discuss the next steps.'],
  'process_label': 'Working together', 'process_title': 'From first contact to completion', 'process_note': 'We agree the details and order of work to suit your task.', 'steps': [['Get in touch', 'Send a message, call me or share a few photographs.'], ['Clarify the details', 'We discuss your wishes, the conditions on site and the intended result.'], ['Agree the scope', 'We agree the work, materials and next steps.'], ['Work and handover', 'After agreement, I carry out the work and discuss the result with you.']],
  'prepare_label': 'Before we talk', 'prepare_title': 'What helps us<br>get started?', 'preparations': [['Photos of the space', 'A few recent photos of the room or area where work is needed.'], ['A short description', 'What would you like to change, and what result do you have in mind?'], ['Your preferred timing', 'An approximate period when you would like the work to begin.']],
  'faq_label': 'Questions and answers', 'faq_title': 'Common questions.', 'faq': [['Can I start by sending photos?', 'Yes. A brief description and a few photos help me get an initial impression. We can clarify further details in a conversation if needed.'], ['How do we discuss materials?', 'Tell me which materials you already have or what result you are looking for. Before work starts, we agree what is needed and who will supply it.'], ['How is the scope agreed?', 'We first discuss your task and the conditions on site. We then clarify the specific work and the next steps.'], ['Where do you work?', 'Frankfurt am Main and the surrounding areas. Please share the location of your property so we can discuss travel.']],
  'contact_label': 'Contact', 'contact_title': 'What would you<br>like to update?', 'contact_intro': 'A few words or photos are enough to start. I will review your enquiry and tell you openly whether I can help.', 'call': 'Call me', 'write': 'Send an email', 'form_title': 'Draft your message', 'name': 'Name', 'contact': 'Phone or email', 'message': 'What needs doing?', 'name_placeholder': 'How should I address you?', 'contact_placeholder': 'How can I get back to you?', 'message_placeholder': 'Briefly describe the task, the space and your wishes', 'submit': 'Open an email draft', 'form_note': 'This form opens your email application. You send the message there; the website does not submit an enquiry automatically.', 'form_status': 'If your email application did not open, please email me directly or use WhatsApp.', 'privacy_link': 'About data processing', 'subject': 'Enquiry from BauServiceMD', 'required': 'required', 'phone_label': 'Phone and WhatsApp', 'email_label': 'Email',
  'footer_line': 'Renovation and assembly. A personal approach to your project.', 'legal_notice': 'The owner is still completing the legal information. This website is a preview.', 'impressum_title': 'Impressum', 'privacy_title': 'Privacy information', 'legal_intro': 'Details of the person responsible for this website', 'address': 'Address', 'owner': 'Owner', 'pending': 'Any further applicable required details and the final wording must be supplied by the owner. Unknown registration and tax numbers have not been added.', 'privacy_intro': 'Information about personal data processing when visiting this website and contacting the tradesperson.', 'privacy_paragraphs': ['Responsible for this website: Renovierungsservice Dmytro Mykhavkiv, Dmytro Mykhavkiv, Ringelstraße 54, 60385 Frankfurt am Main. Contact: renovierungsservicedima@gmail.com.', 'This static website is hosted on GitHub Pages. The hosting provider processes requests when pages are opened. Its privacy statement provides information about that processing.', 'This version has no analytics, advertising trackers, embedded maps or externally loaded web fonts. The website sets no cookies of its own and does not store form entries on a server.', 'Form entries are processed in your browser to create a draft in your email application. You send the message only through your own action in that application. WhatsApp links open an external service, and phone links open your calling application.', 'This is a technical description, not a complete legal privacy policy. Before a commercial launch, the owner needs to provide the full text, including how enquiries are handled, retention periods and visitors’ rights.'], 'github_policy': 'GitHub privacy statement',
  'service_scope': 'What we can discuss', 'service_caveat': 'Each task is assessed individually. This description does not include electrical, plumbing or structural work that requires separate qualifications.', 'back_services': 'Back to all services', 'example_heading': 'An illustrative interior example', 'example_intro': 'This page shows a design direction only. These images were created for the website design and do not show a customer project I have completed.', 'example_body': 'Light surfaces, wooden floors and carefully finished material transitions can help explain your ideas for a room. Send your own photos and describe what you would like to update. We will discuss the possible scope of work separately.', 'back_work': 'Back to the examples', 'contact_page_title': 'Tell me what you have in mind.', 'about_page_title': 'Practical work.<br>Clear agreements.', 'services_page_title': 'My services.', 'projects_page_title': 'Spaces, materials<br>and details.',
 }
}

# Neutral presentation copy: photos are not presented as completed customer commissions.
COPY['uk'].update({
 'hero_alt': 'Світла кімната з дерев’яною підлогою',
 'work_intro': 'Простір, оздоблення та поєднання матеріалів. Перегляньте деталі й розкажіть, що хотіли б змінити у своєму житлі.',
 'example_heading': 'Деталі світлого інтер’єру',
 'example_intro': 'Світлі поверхні, дерев’яне покриття та поєднання фактур у житловому просторі.',
 'back_work': 'До галереї', 'example_link': 'Переглянути деталі', 'all_work': 'До галереї',
 'legal_notice': 'Реквізити Impressum і строк зберігання журналів хостингу ще уточнюються власником.',
})
COPY['de'].update({
 'hero_alt': 'Heller Wohnraum mit Holzfußboden',
 'work_intro': 'Räume, Oberflächen und das Zusammenspiel von Materialien. Sehen Sie sich die Details an und erzählen Sie mir, was Sie verändern möchten.',
 'example_heading': 'Details eines hellen Innenraums',
 'example_intro': 'Helle Oberflächen, Holzfußboden und das Zusammenspiel verschiedener Materialien im Wohnraum.',
 'back_work': 'Zur Galerie', 'example_link': 'Details ansehen', 'all_work': 'Zur Galerie',
 'legal_notice': 'Die Angaben im Impressum und die Speicherdauer der Hosting-Logfiles werden vom Inhaber noch vervollständigt.',
})
COPY['en'].update({
 'hero_alt': 'Bright living room with wooden flooring',
 'work_intro': 'Spaces, finishes and combinations of materials. Explore the details and tell me what you would like to change in your home.',
 'example_heading': 'Details of a bright interior',
 'example_intro': 'Light surfaces, wooden flooring and contrasting textures in a living space.',
 'back_work': 'Back to the gallery', 'example_link': 'View details', 'all_work': 'View the gallery',
 'legal_notice': 'The owner is still completing the Impressum details and the hosting log retention period.',
})


for lang, values in {
    'uk': ('Галерея', 'Відкрити фото', 'Закрити', 'Попереднє фото', 'Наступне фото', 'Перегляньте фото інтер’єрів та деталей оздоблення. Натисніть на фото, щоб збільшити.'),
    'de': ('Galerie', 'Foto öffnen', 'Schließen', 'Vorheriges Foto', 'Nächstes Foto', 'Entdecken Sie Innenräume und Details der Ausführung. Klicken Sie auf ein Foto, um es zu vergrößern.'),
    'en': ('Gallery', 'Open photo', 'Close', 'Previous photo', 'Next photo', 'Explore interiors and finishing details. Select a photo to enlarge it.'),
}.items():
    for key, value in zip(('projects_page_title', 'example_link', 'gallery_close', 'gallery_prev', 'gallery_next', 'work_intro'), values):
        COPY[lang][key] = value


# Presentation copy uses unpunctuated labels and short editorial blurbs.
# Keep natural paragraph punctuation and the supplied legal policy unchanged.
def presentation_label(value):
    return value.replace('.<br>', '<br>').rstrip().rstrip('.')

for localized in COPY.values():
    for key, value in localized.items():
        if isinstance(value, str) and (
            key.endswith(('_title', '_heading', '_label'))
            or key in {'connect', 'menu', 'skip', 'home', 'hero_cta', 'view_work',
                       'all_services', 'details', 'all_work', 'example_detail',
                       'example_wide', 'example_link', 'about_more', 'call',
                       'write', 'name', 'contact', 'message', 'submit',
                       'privacy_link', 'back_services', 'back_work', 'address',
                       'owner', 'service_scope'}
        ):
            localized[key] = presentation_label(value)
    localized['nav'] = [presentation_label(item) for item in localized['nav']]
    for collection in ('services', 'steps', 'preparations'):
        for item in localized[collection]:
            item[0] = presentation_label(item[0])
            # Multi-sentence paragraphs keep their sentence punctuation.
            if item[1].count('.') == 1 and item[1].endswith('.'):
                item[1] = item[1][:-1]


SLUGS = ['index.html', 'services.html', 'service-renovation.html', 'service-flooring.html', 'service-assembly.html', 'service-repairs.html', 'projects.html', 'project-example.html', 'about.html', 'contact.html', 'impressum.html', 'privacy.html']
SERVICE_SLUGS = SLUGS[2:6]

def text(s):
    return esc(s, quote=True)

def arrow(cls=''):
    return f'<svg class="icon-arrow {cls}" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 19 19 5M5 5h14v14"/></svg>'

def link(href, label, cls='text-link'):
    return f'<a class="{cls}" href="{href}">{text(label)} {arrow()}</a>'

def image(filename, alt, cls='', eager=False):
    contextual = {
        'Ілюстративне зображення': {'work': 'Руки майстра під час вимірювання дерев’яного елемента', 'detail': 'Стик дерев’яної підлоги, плінтуса та оздобленої стіни', 'room': 'Світла кімната з дерев’яним підлоговим покриттям', 'hero': 'Світлий житловий простір із природними матеріалами'},
        'Illustrative Abbildung': {'work': 'Hände eines Handwerkers beim Vermessen eines Holzelements', 'detail': 'Übergang zwischen Holzboden, Sockelleiste und Wand', 'room': 'Heller Raum mit Holzfußboden', 'hero': 'Heller Wohnraum mit natürlichen Materialien'},
        'Illustrative image': {'work': 'A tradesperson’s hands measuring a piece of wood', 'detail': 'Junction between a wooden floor, skirting board and finished wall', 'room': 'Bright room with wooden flooring', 'hero': 'Bright living space with natural materials'},
    }
    alt = contextual.get(alt, {}).get(filename, alt)
    for prefix in ('Ілюстрація: ', 'Ілюстрація ', 'Illustration: ', 'Illustration of ', 'Illustration eines ', 'Illustration des '):
        if alt.startswith(prefix):
            alt = alt[len(prefix):]
            break
    if alt:
        alt = alt[0].upper() + alt[1:]
    return f'<img src="../assets/images/{filename}.webp" alt="{text(alt)}" width="1400" height="1000" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async"{ " fetchpriority=\"high\"" if eager else ""}>'

def label(number, title, numbered=True):
    prefix = f'<span>{text(number)}</span> ' if numbered else ''
    return f'<p class="eyebrow section-label">{prefix}{text(title)}</p>'

def title_plain(title):
    return title.replace('<br>', ' ')

def header(lang, slug, c):
    nav = ''.join(f'<a href="{s}"{ " aria-current=\"page\"" if slug == s or (s == "services.html" and slug in SERVICE_SLUGS) or (s == "projects.html" and slug == "project-example.html") else ""}>{text(t)}</a>' for s,t in zip(['services.html','projects.html','about.html','contact.html'], c['nav']))
    languages = ''.join(f'<a href="../{l}/{slug}" lang="{l}" hreflang="{l}" aria-label="{COPY[l]["lang_name"]}"{ " aria-current=\"true\"" if l == lang else ""}>{"UA" if l == "uk" else l.upper()}</a>' for l in COPY)
    language_label = {'uk': 'Мова сайту', 'de': 'Sprache', 'en': 'Language'}[lang]
    return f'''<a class="skip-link" href="#main">{c['skip']}</a>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="index.html" aria-label="BauServiceMD — {c['home']}"><img src="../assets/images/logo.webp" alt="BauServiceMD — Renovierung &amp; Innenausbau" width="260" height="172"></a>
<nav class="site-nav" id="mobile-menu" data-menu aria-label="{c['menu']}">{nav}</nav>
<div class="header-actions"><nav class="language-switcher" aria-label="{language_label}">{languages}</nav>{link('contact.html', c['connect'], 'button button-secondary header-contact')}
<button class="menu-toggle" type="button" data-menu-toggle aria-controls="mobile-menu" aria-expanded="false"><span>{c['menu']}</span><span class="menu-icon" aria-hidden="true"><span></span><span></span></span></button></div>
</div></header>'''

def footer(c):
    nav = ''.join(f'<a href="{s}">{text(t)}</a>' for s,t in zip(['services.html','projects.html','about.html','contact.html'],c['nav']))
    return f'''<footer class="site-footer"><div class="container footer-grid">
<div><a class="brand footer-brand" href="index.html"><img src="../assets/images/logo.webp" alt="BauServiceMD" width="260" height="172" loading="lazy"></a><p>{text(c['footer_line'])}</p></div>
<nav class="footer-links" aria-label="{c['menu']}">{nav}</nav>
<div class="footer-contact"><a href="tel:+4915778582592">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><p>{text(c['region'])}</p></div>
<div class="footer-legal"><a href="impressum.html">Impressum</a><a href="privacy.html">Datenschutzerklärung</a></div>
</div><div class="container legal-notice"><p>{text(c['legal_notice'])}</p></div></footer>'''

def form(c):
    return f'''<form class="contact-form" data-contact-form data-subject="{text(c['subject'])}" data-fallback="{text(c['form_status'])}" action="mailto:{EMAIL}" method="post" enctype="text/plain">
<div class="form-row"><div class="form-field"><label for="contact-name">{text(c['name'])} <span aria-hidden="true">*</span></label><input id="contact-name" name="name" type="text" autocomplete="name" maxlength="120" required placeholder="{text(c['name_placeholder'])}"></div>
<div class="form-field"><label for="contact-reply">{text(c['contact'])} <span aria-hidden="true">*</span></label><input id="contact-reply" name="contact" type="text" autocomplete="email" maxlength="180" required placeholder="{text(c['contact_placeholder'])}"></div></div>
<div class="form-field"><label for="contact-message">{text(c['message'])} <span aria-hidden="true">*</span></label><textarea id="contact-message" name="message" rows="5" maxlength="4000" required placeholder="{text(c['message_placeholder'])}"></textarea></div>
<button class="button button-primary" type="submit">{text(c['submit'])} {arrow()}</button>
<p class="form-note">{text(c['form_note'])}</p><a class="text-link" href="privacy.html">{text(c['privacy_link'])}</a><p class="form-status" data-form-status role="status" aria-live="polite"></p></form>'''

def contact_section(c, full=False):
    details = f'''<dl class="contact-details"><div><dt>{text(c['phone_label'])}</dt><dd><a href="tel:+4915778582592">{PHONE}</a></dd></div><div><dt>{text(c['email_label'])}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>{text(c['region'])}</dt><dd>Frankfurt am Main, Deutschland</dd></div></dl>''' if full else ''
    return f'''<section class="section contact-section" id="contact" aria-labelledby="contact-heading"><div class="container contact-grid"><div class="contact-copy">{label('07',c['contact_label'],c.get('section_numbers', True))}<h2 id="contact-heading">{c['contact_title']}</h2><p>{text(c['contact_intro'])}</p><div class="contact-options">{link(WA,'WhatsApp','button button-secondary')}{link('tel:+4915778582592',c['call'],'button button-secondary')}</div><p><a class="text-link" href="mailto:{EMAIL}">{text(c['write'])} {arrow()}</a></p>{details}</div><div><h3 class="form-heading">{text(c['form_title'])}</h3>{form(c)}</div></div></section>'''

def service_list(c):
    return '<div class="service-list">' + ''.join(f'''<a class="service-row" href="{slug}"><span class="service-number">0{i+1}</span><div class="service-content"><h3>{text(item[0])}</h3><p>{text(item[1])}</p></div>{arrow('service-arrow')}</a>''' for i,(slug,item) in enumerate(zip(SERVICE_SLUGS,c['services']))) + '</div>'

def service_section(c):
    return f'''<section class="section services-section" aria-labelledby="services-heading"><div class="container services-layout"><div class="services-intro">{label('01',c['services_label'],c.get('section_numbers', True))}<h2 id="services-heading">{c['services_title']}</h2><p>{text(c['services_intro'])}</p><figure>{image('detail',c['illustration'])}</figure></div><div>{service_list(c)}<p class="section-note">{text(c['services_note'])}</p>{link('services.html',c['all_services'])}</div></div></section>'''

def projects_grid(c, expanded=False):
    cards = [('room', c['example_title'], ''), ('detail', c['example_detail'], ''), ('hero', c['example_wide'], 'project-card-wide')]
    if not expanded:
        cards = cards[:2]
    return '<div class="project-grid">'+''.join(f'''<article class="project-card {cls}"><a href="../assets/images/{filename}.webp" data-gallery-image data-caption="{text(title)}" aria-label="{text(c['example_link'])}: {text(title)}">{image(filename,title)}</a><div class="project-copy"><h3>{text(title)}</h3><a class="text-link" href="../assets/images/{filename}.webp" data-gallery-image data-caption="{text(title)}">{text(c['example_link'])}{arrow()}</a></div></article>''' for filename,title,cls in cards)+'</div>'

def gallery_dialog(c):
    return f'''<dialog class="gallery-dialog" aria-label="{text(c['projects_page_title'])}" data-gallery-dialog><div class="gallery-toolbar"><p data-gallery-counter aria-live="polite"></p><button type="button" class="gallery-control" data-gallery-close>{text(c['gallery_close'])}<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="m6 6 12 12M6 18 18 6"/></svg></button></div><figure><img data-gallery-photo alt=""><figcaption data-gallery-caption></figcaption></figure><div class="gallery-navigation"><button type="button" class="gallery-control" data-gallery-prev aria-label="{text(c['gallery_prev'])}">{arrow('gallery-arrow-prev')}</button><button type="button" class="gallery-control" data-gallery-next aria-label="{text(c['gallery_next'])}">{arrow('gallery-arrow-next')}</button></div></dialog>'''

def projects_section(c):
    return f'''<section class="section projects-section" aria-labelledby="projects-heading"><div class="container"><div class="section-top"><div>{label('02',c['work_label'],c.get('section_numbers', True))}<h2 id="projects-heading">{text(c['work_title'])}</h2></div>{link('projects.html',c['all_work'])}</div><p class="section-intro">{text(c['work_intro'])}</p>{projects_grid(c,True)}</div></section>'''

def about_section(c):
    return f'''<section class="about-band section" aria-labelledby="about-heading"><div class="container about-band-grid"><div>{label('03',c['about_label'],c.get('section_numbers', True))}<h2 id="about-heading">{c['about_title']}</h2></div><div><p>{text(c['about_short'])}</p>{link('about.html',c['about_more'])}</div><figure>{image('work',c['illustration'])}</figure></div></section>'''

def process_section(c):
    steps = ''.join(f'<li class="step"><span class="step-number">0{i+1}</span><h3>{text(t)}</h3><p>{text(b)}</p></li>' for i,(t,b) in enumerate(c['steps']))
    return f'''<section class="section process-section" aria-labelledby="process-heading"><div class="container">{label('04',c['process_label'],c.get('section_numbers', True))}<div class="section-top"><h2 id="process-heading">{text(c['process_title'])}</h2><p class="section-note">{text(c['process_note'])}</p></div><ol class="steps">{steps}</ol></div></section>'''

def prepare_section(c):
    rows = ''.join(f'<li><span class="service-number">0{i+1}</span><div><h3>{text(t)}</h3><p>{text(b)}</p></div></li>' for i,(t,b) in enumerate(c['preparations']))
    return f'''<section class="section preparation-section" aria-labelledby="prepare-heading"><div class="container preparation-grid"><div>{label('05',c['prepare_label'],c.get('section_numbers', True))}<h2 id="prepare-heading">{c['prepare_title']}</h2><figure>{image('detail',c['illustration'])}</figure></div><ul class="preparation-list">{rows}</ul></div></section>'''

def faq_section(c):
    rows = ''.join(f'<details{ " open" if i == 0 else ""}><summary>{text(q)}<span aria-hidden="true">+</span></summary><p>{text(a)}</p></details>' for i,(q,a) in enumerate(c['faq']))
    return f'''<section class="section faq-section" aria-labelledby="faq-heading"><div class="container faq-layout"><div>{label('06',c['faq_label'],c.get('section_numbers', True))}<h2 id="faq-heading">{text(c['faq_title'])}</h2></div><div class="faq-list">{rows}</div></div></section>'''

def homepage(c):
    return f'''<section class="container hero" aria-labelledby="hero-heading"><div class="hero-copy"><p class="eyebrow">{text(c['private'])} · {text(c['region'])}</p><h1 id="hero-heading" class="hero-title">{c['hero_title']}</h1><p class="hero-description">{text(c['hero_description'])}</p><div class="hero-actions">{link('contact.html',c['hero_cta'],'button button-primary')}{link('projects.html',c['view_work'])}</div><figure class="hero-detail">{image('detail',c['illustration'])}</figure></div><figure class="hero-media">{image('hero',c['hero_alt'],eager=True)}</figure></section>{service_section(c)}{projects_section(c)}{about_section(c)}{process_section(c)}{prepare_section(c)}{faq_section(c)}{contact_section(c)}'''

def page_hero(c, title, subtitle='', crumb=None):
    return f'''<section class="section page-hero"><div class="container"><nav class="breadcrumbs" aria-label="{text(c['home'])}"><a href="index.html">{text(c['home'])}</a><span aria-hidden="true">/</span><span>{text(crumb or title_plain(title))}</span></nav><h1>{title}</h1>{f'<p class="section-intro">{text(subtitle)}</p>' if subtitle else ''}</div></section>'''

def page(lang, slug, c):
    if slug == 'index.html':
        return homepage(c), title_plain(c['hero_title']), c['hero_description']
    if slug == 'services.html':
        return page_hero(c,c['services_page_title'],c['services_intro'])+f'<section class="section"><div class="container services-layout"><figure>{image("work",c["illustration"],eager=True)}</figure><div>{service_list(c)}<p class="section-note">{text(c["services_note"])}</p></div></div></section>'+process_section(c)+contact_section(c),c['services_page_title'],c['services_intro']
    if slug in SERVICE_SLUGS:
        i=SERVICE_SLUGS.index(slug)
        item=c['services'][i]
        body=page_hero(c,text(item[0]),item[1])+f'''<section class="section"><div class="container service-detail-grid"><figure>{image('work' if i in [0,2,3] else 'detail',c['illustration'],eager=True)}</figure><div class="prose"><h2>{text(c['service_scope'])}</h2><ul class="detail-list">{''.join(f'<li>{text(s)}</li>' for s in item[2])}</ul><p>{text(c['services_note'])}</p><p class="section-note">{text(c['service_caveat'])}</p>{link('services.html',c['back_services'])}</div></div></section>'''+prepare_section(c)+contact_section(c)
        return body,item[0],item[1]
    if slug=='projects.html':
        return page_hero(c,c['projects_page_title'],c['work_intro'])+f'<section class="section"><div class="container">{projects_grid(c,True)}</div></section>'+contact_section(c),c['work_label'],c['work_intro']
    if slug=='project-example.html':
        return page_hero(c,c['example_heading'],c['example_intro'])+f'''<section class="section"><div class="container"><figure class="example-hero">{image('room',c['illustration'],eager=True)}</figure><div class="prose example-prose"><p>{text(c['example_body'])}</p>{link('projects.html',c['back_work'])}</div></div></section>'''+contact_section(c),c['example_heading'],c['example_intro']
    if slug=='about.html':
        return page_hero(c,c['about_page_title'])+f'''<section class="section"><div class="container page-grid"><div class="prose"><h2>Dmytro Mykhavkiv</h2><p>{text(c['about_short'])}</p>{''.join(f'<p>{text(p)}</p>' for p in c['about_paragraphs'])}</div><figure>{image('work',c['illustration'],eager=True)}</figure></div></section>'''+process_section(c)+contact_section(c),c['about_label'],c['about_short']
    if slug=='contact.html':
        return page_hero(c,c['contact_page_title'],c['contact_intro'])+contact_section(c,True)+faq_section(c),c['contact_label'],c['contact_intro']
    if slug=='impressum.html':
        return page_hero(c,c['impressum_title'],c['legal_intro'])+f'''<section class="section"><div class="container prose legal-prose"><h2>Renovierungsservice Dmytro Mykhavkiv</h2><dl class="contact-details"><div><dt>{text(c['owner'])}</dt><dd>Dmytro Mykhavkiv</dd></div><div><dt>{text(c['address'])}</dt><dd>Ringelstraße 54<br>60385 Frankfurt am Main<br>Deutschland</dd></div><div><dt>{text(c['phone_label'])}</dt><dd><a href="tel:+4915778582592">{PHONE}</a></dd></div><div><dt>{text(c['email_label'])}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div></dl><p class="notice">{text(c['pending'])}</p></div></section>''',c['impressum_title'],c['legal_intro']
    return page_hero(c,TITLES[lang],c['privacy_intro'])+f'''<section class="section"><div class="container prose legal-prose">{POLICY[lang]}</div></section>''',TITLES[lang],c['privacy_intro']

def document(lang, slug):
    c={**COPY[lang], 'section_numbers': slug == 'index.html'}
    body,title,description=page(lang,slug,c)
    alternates=''.join(f'<link rel="alternate" hreflang="{l}" href="{BASE}/{l}/{slug}">' for l in COPY)
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><title>{text(title_plain(title))} | BauServiceMD</title><meta name="description" content="{text(description)}"><link rel="canonical" href="{BASE}/{lang}/{slug}">{alternates}<link rel="alternate" hreflang="x-default" href="{BASE}/uk/{slug}"><meta property="og:type" content="website"><meta property="og:site_name" content="BauServiceMD"><meta property="og:title" content="{text(title_plain(title))} | BauServiceMD"><meta property="og:description" content="{text(description)}"><meta property="og:url" content="{BASE}/{lang}/{slug}"><meta property="og:image" content="{BASE}/assets/images/hero.webp"><link rel="icon" href="../assets/images/favicon.png" type="image/png"><link rel="stylesheet" href="../assets/css/base.css"><link rel="stylesheet" href="../assets/css/layout.css"><link rel="stylesheet" href="../assets/css/components.css"><link rel="stylesheet" href="../assets/css/pages.css"><link rel="stylesheet" href="../assets/css/motion.css"><script src="../assets/js/main.js" defer></script><script src="../assets/js/motion.js" defer></script></head><body>{header(lang,slug,c)}<main id="main">{body}</main>{gallery_dialog(c) if slug in ("index.html", "projects.html") else ""}{footer(c)}</body></html>
'''

def build():
    for lang in COPY:
        (ROOT/lang).mkdir(exist_ok=True)
        for slug in SLUGS:
            (ROOT/lang/slug).write_text(document(lang,slug),encoding='utf-8')
    # A real Ukrainian landing page at the repository root, not an automatic language redirect.
    root=document('uk','index.html').replace('../assets/','assets/').replace('href="../uk/','href="uk/').replace('href="../de/','href="de/').replace('href="../en/','href="en/')
    # Local page links become uk/*; external links and fragments remain unchanged.
    for slug in SLUGS:
        root=root.replace(f'href="{slug}"',f'href="uk/{slug}"')
    (ROOT/'index.html').write_text(root,encoding='utf-8')
    urls = [f'{BASE}/{lang}/{slug}' for lang in COPY for slug in SLUGS]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{url}</loc></url>\n' for url in urls) + '</urlset>\n'
    (ROOT/'sitemap.xml').write_text(sitemap, encoding='utf-8')
    (ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n', encoding='utf-8')
    print(f'Generated {len(COPY)*len(SLUGS)+1} HTML pages and sitemap.')

if __name__=='__main__':
    build()
