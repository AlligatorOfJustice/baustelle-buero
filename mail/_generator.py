# Erzeugt die E-Mail-Vorlagen für Brevo (tabellenbasiert, Inline-Styles).
OUT = '/home/claude/baustelle-buero/mail/'
SITE = 'https://www.baustelle-buero.ch'
LOGO = SITE + '/mail/logo.png'
INK, MUTED, LINE, BG, PRI, PRI_SOFT, ACC, ACC_SOFT = '#13232B', '#5A6A72', '#DAE2E5', '#F2F5F6', '#0E5A6B', '#E1EEF1', '#E2762A', '#FBEADD'
HEAD = "'Red Hat Display', Arial, Helvetica, sans-serif"
BODY = "'Red Hat Text', Arial, Helvetica, sans-serif"

def shell(title, preheader, content, footer):
    return f'''<!doctype html>
<html lang="de" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@700;800&family=Red+Hat+Text:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  body{{margin:0;padding:0;background:{BG};-webkit-text-size-adjust:100%;}}
  table{{border-collapse:collapse;}}
  img{{border:0;line-height:100%;outline:none;text-decoration:none;}}
  a{{color:{PRI};}}
  @media (max-width:620px){{
    .card{{width:100%!important;border-radius:0!important;}}
    .pad{{padding-left:22px!important;padding-right:22px!important;}}
    .h1{{font-size:26px!important;line-height:32px!important;}}
    .btn a{{display:block!important;}}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:{BG};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{BG};">{preheader}&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{BG};">
  <tr><td align="center" style="padding:24px 12px;">
    <table role="presentation" class="card" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:#FFFFFF;border:1px solid {LINE};border-radius:12px;">
      <tr><td class="pad" style="padding:28px 40px 20px 40px;border-bottom:1px solid {LINE};">
        <a href="{SITE}" style="text-decoration:none;"><img src="{LOGO}" width="200" height="38" alt="baustelle-büro" style="display:block;width:200px;height:38px;"></a>
      </td></tr>
{content}
    </table>
    <table role="presentation" width="600" class="card" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">
      <tr><td class="pad" style="padding:20px 40px 8px 40px;font-family:{BODY};font-size:12.5px;line-height:19px;color:{MUTED};">
{footer}
      </td></tr>
    </table>
  </td></tr>
</table>
</body>
</html>
'''

def row(inner, pad='0 40px 0 40px'):
    return f'''      <tr><td class="pad" style="padding:{pad};">
{inner}
      </td></tr>'''

def kicker(t): return f'<p style="margin:0 0 6px 0;font-family:{BODY};font-size:14px;line-height:20px;font-weight:700;color:{PRI};">{t}</p>'
def h1(t): return f'<h1 class="h1" style="margin:0 0 16px 0;font-family:{HEAD};font-size:30px;line-height:36px;font-weight:800;color:{INK};">{t}</h1>'
def h2(t): return f'<h2 style="margin:0 0 8px 0;font-family:{HEAD};font-size:20px;line-height:26px;font-weight:800;color:{INK};">{t}</h2>'
def p(t, mb=16, size=16, color=INK): return f'<p style="margin:0 0 {mb}px 0;font-family:{BODY};font-size:{size}px;line-height:{int(size*1.55)}px;color:{color};">{t}</p>'
def btn(label, href, color=PRI):
    return f'''<table role="presentation" class="btn" cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 20px 0;"><tr><td align="center" bgcolor="{color}" style="border-radius:8px;background:{color};">
<a href="{href}" style="display:inline-block;padding:14px 26px;font-family:{BODY};font-size:16px;line-height:20px;font-weight:700;color:#FFFFFF;text-decoration:none;border-radius:8px;">{label}</a>
</td></tr></table>'''
def box(inner, bg=PRI_SOFT, border=None):
    b = f'border:1.5px solid {border};' if border else ''
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 24px 0;"><tr><td style="padding:20px 22px 4px 22px;background:{bg};{b}border-radius:10px;">
{inner}
</td></tr></table>'''
def ul(items):
    lis = ''.join(f'<tr><td valign="top" style="width:22px;padding:0 0 8px 0;font-family:{BODY};font-size:16px;line-height:24px;color:{ACC};font-weight:700;">–</td><td style="padding:0 0 8px 0;font-family:{BODY};font-size:16px;line-height:24px;color:{INK};">{t}</td></tr>' for t in items)
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 16px 0;">{lis}</table>'
def sign(): return p(f'Herzliche Grüsse<br><strong>Florian</strong><br><span style="color:{MUTED};">baustelle-büro</span>', mb=0)
ADDR = 'baustelle-büro · Florian Buchs · Karl Haueter-Strasse 5 · 3770 Zweisimmen'
def flinks(*links): return ' · '.join(f'<a href="{h}" style="color:{MUTED};text-decoration:underline;">{t}</a>' for t,h in links)

# 1) Double-Opt-in (keine Werbung, nur Bestätigung)
doi = shell('Bitte bestätige deine Anmeldung', 'Ein Klick, dann bist du dabei.',
 row(kicker('Büro-Brief') + h1('Fast geschafft') +
     p('Danke für dein Interesse am Büro-Brief von baustelle-büro. Bitte bestätige mit einem Klick, dass du ihn erhalten möchtest.') +
     btn('Anmeldung bestätigen', '{{ doubleoptin }}') +
     p(f'Mit dem Klick willigst du ein, dass wir dir den Büro-Brief einmal im Monat per E-Mail schicken. Du kannst ihn jederzeit mit einem Klick abbestellen. Mehr dazu in der <a href="{SITE}/#datenschutz" style="color:{PRI};">Datenschutzerklärung</a>.', size=14, color=MUTED) +
     p('Du hast dich nicht angemeldet? Dann ignoriere diese E-Mail einfach. Ohne Bestätigung erhältst du keine weiteren Nachrichten.', size=14, color=MUTED, mb=24) +
     sign(), pad='28px 40px 32px 40px'),
 f'{ADDR}<br>' + flinks(('baustelle-buero.ch', SITE), ('Impressum', SITE + '/#impressum'), ('Datenschutz', SITE + '/#datenschutz')))
open(OUT + 'double-opt-in.html', 'w', encoding='utf-8').write(doi)

# 2) Willkommen (finale Bestätigung)
welcome = shell('Willkommen beim Büro-Brief', 'Das erwartet dich und ein erster Tipp für heute.',
 row(kicker('Büro-Brief') + h1('Schön, dass du dabei bist') +
     p('Ich bin Florian: gelernter Koch, danach Landschaftsgärtner und Gartenbautechniker HF. Ich arbeite gern mit den Händen. Schon als Kind habe ich Computer zusammengebaut und eingerichtet.') +
     p('Im Handwerk habe ich eine Szene immer wieder erlebt: Ein Kunde ruft an und fragt nach der Offerte. Wurde sie schon verschickt? Oder noch gar nicht erstellt? Niemand weiss es, weil das Wissen bei der Person liegt, die gerade auf der Baustelle ist.') +
     p('In meiner Diplomarbeit habe ich mit Handwerksbetrieben darüber gesprochen. Das Überraschende: Fast allen geht es gleich. Und das Problem ist selten die Technik, sondern wie man im Team mit Daten umgeht. Genau da setzt baustelle-büro an.') +
     h2('Was dich erwartet') +
     ul(['Einmal im Monat ein Tipp, den du in 15 Minuten umsetzen kannst', 'Vorlagen, die du direkt im Betrieb brauchen kannst', 'Kein Fachchinesisch und keine Werbeflut']) +
     '<!-- PLATZ FÜR GRATIS-VORLAGE: Sobald die Ordnerstruktur bereit ist, hier eine Box mit Download-Button einfügen. -->\n' +
     box(kicker('Dein erster Tipp') + h2('Dateinamen, die man wiederfindet') +
         p('Benenne jede Datei nach dem gleichen Muster: Datum, Projekt, Inhalt, Version. Zum Beispiel <strong>261027_Gartenumbau-Mueller_Offerte_v1.pdf</strong>. So findest du jede Datei in Sekunden, auch die vom letzten Jahr.') +
         btn('Zum Dateinamen-Generator', SITE + '/#werkzeuge')) +
     p(f'Noch nicht gemacht? Der <a href="{SITE}" style="color:{PRI};font-weight:700;">Büro-Check</a> zeigt dir in fünf Minuten, wo dein Betrieb steht.') +
     p('Und eine Bitte: Antworte kurz auf diese E-Mail und schreib mir, was dich im Büro am meisten nervt. Ich lese jede Antwort. Die besten Fragen beantworte ich im Büro-Brief.', mb=24) +
     sign(), pad='28px 40px 32px 40px'),
 f'Du erhältst diese E-Mail, weil du dich auf baustelle-buero.ch für den Büro-Brief angemeldet hast. Abmelden kannst du dich jederzeit über den Link am Ende jedes Büro-Briefs.<br><br>{ADDR}<br>' + flinks(('Impressum', SITE + '/#impressum'), ('Datenschutz', SITE + '/#datenschutz')))
open(OUT + 'willkommen.html', 'w', encoding='utf-8').write(welcome)

# 3) Grundvorlage Büro-Brief
brief = shell('Büro-Brief', '[Vorschautext: ein Satz, der neugierig macht]',
 row(f'<p style="margin:0 0 6px 0;font-family:{BODY};font-size:14px;line-height:20px;font-weight:700;color:{PRI};">Büro-Brief Nr. [1] · [Datum]</p>' +
     h1('[Titel: das Problem in einem Satz]') +
     p('[Einstieg: zwei bis drei Sätze aus dem Büroalltag. Warum ist das Thema wichtig?]'), pad='28px 40px 4px 40px') + '\n' +
 row(kicker('Tipp') + h2('[Der Tipp in einem Satz]') +
     p('[Kurz erklärt, was zu tun ist. Höchstens fünf Sätze oder drei Schritte.]') +
     ul(['[Schritt 1]', '[Schritt 2]', '[Schritt 3]'])) + '\n' +
 row(box(kicker('Vorlage') + h2('[Name der Vorlage]') +
         p('[Wofür sie gut ist, in einem Satz.]') +
         btn('Vorlage herunterladen', '[Link zur Vorlage]'))) + '\n' +
 row(kicker('Aus der Werkstatt') +
     p('[Kurz, was es Neues gibt bei baustelle-büro: Zahl der Checks, Feedback, nächster Schritt. Zwei bis drei Sätze.]')) + '\n' +
 row(box(kicker('<span style="color:' + ACC + ';">Toolkit «Ordnung im Betrieb»</span>') +
         p('Alle Merkblätter, Vorlagen und die Excel-Arbeitsmappe, um die Massnahmen mit deinem Team umzusetzen.') +
         btn('Toolkit ansehen · CHF 29', SITE + '/#toolkit', color=ACC), bg='#FFFFFF', border=ACC)) + '\n' +
 row(p('[Abschluss: eine Frage an die Leser, zum Beispiel «Wie macht ihr das? Antworte einfach auf diese Mail.»]', mb=24) + sign(), pad='0 40px 32px 40px'),
 f'Du erhältst diese E-Mail, weil du dich auf baustelle-buero.ch für den Büro-Brief angemeldet hast.<br>' +
 flinks(('Abmelden', '{{ unsubscribe }}'), ('Im Browser ansehen', '{{ mirror }}'), ('Impressum', SITE + '/#impressum')) +
 f'<br><br>{ADDR}')
open(OUT + 'buero-brief-vorlage.html', 'w', encoding='utf-8').write(brief)

# 4) Mailfolge nach Toolkit-Kauf (Brevo-Automation, Liste «Toolkit-Käufer»: Tag 2, 7, 14)
UTM = '?utm_source=brevo&utm_medium=email&utm_campaign=toolkit-folge'
HALLO = 'Hallo {{ contact.VORNAME | default : "zusammen" }}'
def ol(items):
    lis = ''.join(f'<tr><td valign="top" style="width:30px;padding:0 0 12px 0;"><span style="display:inline-block;width:22px;height:22px;border-radius:11px;background:{PRI};color:#FFFFFF;font-family:{BODY};font-size:13px;line-height:22px;font-weight:700;text-align:center;">{i}</span></td><td style="padding:0 0 12px 0;font-family:{BODY};font-size:16px;line-height:24px;color:{INK};">{t}</td></tr>' for i, t in enumerate(items, 1))
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 16px 0;">{lis}</table>'
FOLGE_FOOTER = (f'Du erhältst diese E-Mail, weil du das Toolkit «Ordnung im Betrieb» gekauft hast. Diese Reihe umfasst drei kurze Mails.<br>' +
    flinks(('Abmelden', '{{ unsubscribe }}'), ('Impressum', SITE + '/#impressum'), ('Datenschutz', SITE + '/#datenschutz')) + f'<br><br>{ADDR}')
def folge(nr, title, preheader, inner):
    return shell(title, preheader, row(kicker(f'Toolkit «Ordnung im Betrieb» · {nr} von 3') + inner + sign(), pad='28px 40px 32px 40px'), FOLGE_FOOTER)

f1 = folge(1, 'Eine Massnahme, diese Woche', 'Nicht alles auf einmal. Eine Sache, die in einer Stunde erledigt ist.',
  h1('Eine Massnahme, diese Woche') +
  p(f'{HALLO}') +
  p('Du hast das Toolkit jetzt seit einigen Tagen. Vielleicht hast du schon reingeschaut, vielleicht liegt es noch im Download-Ordner. Beides ist normal. Damit es nicht dort bleibt, nimm dir diese Woche genau eine Sache vor:') +
  ol(['<strong>Eine Massnahme wählen,</strong> die du in höchstens einer Stunde erledigen kannst. Zum Beispiel: eine Ablageregel festlegen oder bestimmen, wer Offerten verschickt.',
      '<strong>Name und Datum eintragen,</strong> im Blatt «Massnahmen» der Excel-Arbeitsmappe. Was kein Datum hat, passiert nicht.',
      '<strong>Dem Team sagen,</strong> beim Znüni oder in der nächsten Besprechung. Zwei Sätze reichen: was sich ändert und ab wann.']) +
  box(kicker('Tipp') + h2('Mach es nicht allein') +
      p('Lass zwei Leute aus dem Team die gleichen Fragen im Reifegradmodell beantworten. Wo eure Antworten auseinandergehen, liegt meist das eigentliche Problem.')) +
  p('Hast du keine Dateien erhalten oder lässt sich etwas nicht öffnen? Antworte einfach auf diese Mail, dann schicke ich sie dir nochmals.') +
  p('In ein paar Tagen zeige ich dir, wie du mit dem Team in 30 Minuten klärst, wer wofür zuständig ist.', mb=24))
open(OUT + 'toolkit-folge-1.html', 'w', encoding='utf-8').write(f1)

f2 = folge(2, 'Wer macht eigentlich was?', 'Zuständigkeiten klären, in 30 Minuten und mit einer Tabelle.',
  h1('Wer macht eigentlich was?') +
  p(f'{HALLO}') +
  p('Die Offerte, die niemand verschickt hat, ist fast nie ein Technikproblem. Meist fühlt sich einfach niemand zuständig. Alle helfen mit, aber keiner steht dafür gerade.') +
  h2('So gehst du mit der RACI-Vorlage vor') +
  ol(['<strong>Fünf Aufgaben wählen,</strong> die jede Woche vorkommen. Zum Beispiel: Offerte schreiben, Material bestellen, Rapport abgeben, Rechnung stellen, Reklamation bearbeiten.',
      '<strong>30 Minuten mit dem Team.</strong> Tragt pro Aufgabe ein, wer sie erledigt (R) und wer dafür geradesteht (A).',
      '<strong>Pro Aufgabe genau ein A.</strong> Stehen zwei Namen da, ist es am Ende niemand.',
      '<strong>Prüfen lassen.</strong> Das Blatt «RACI» in der Excel-Arbeitsmappe zeigt dir, wo ein A fehlt oder doppelt vergeben ist.']) +
  box(kicker('Tipp') + h2('Erst das Beispiel anschauen') +
      p('Im Toolkit findest du eine ausgefüllte RACI-Matrix aus einem Gartenbaubetrieb. Sie zeigt, wie konkret die Einträge sein dürfen.')) +
  p('Häng die fertige Tabelle dort auf, wo das Team sie sieht: im Büro, im Pausenraum oder im Baustellenwagen.') +
  p('Nächste Woche geht es darum, wie du dranbleibst, damit das Ganze nicht nach drei Wochen wieder einschläft.', mb=24))
open(OUT + 'toolkit-folge-2.html', 'w', encoding='utf-8').write(f2)

CAL_ON = 'https://cal.com/baustelle-buero/buero-check-online' + UTM
CAL_VO = 'https://cal.com/baustelle-buero/buero-check-vor-ort' + UTM
f3 = folge(3, 'Damit es nicht wieder einschläft', 'Zwei kleine Gewohnheiten und Hilfe, wenn du sie willst.',
  h1('Damit es nicht wieder einschläft') +
  p(f'{HALLO}') +
  p('Nach zwei Wochen lässt der Schwung oft nach. Das ist normal. Zwei Dinge helfen, dass die Ordnung bleibt:') +
  ul(['<strong>Eine Übergabe fix regeln:</strong> Nimm das Formular «Auftragsstart» und nutz es beim nächsten Auftrag. Nur eines, nur einmal.',
      '<strong>Den nächsten Check jetzt eintragen:</strong> Setz dir heute einen Termin in drei Monaten. Der Leitfaden im Toolkit führt dich durch die Stunde.']) +
  box(kicker('Büro-Check 1:1') + h2('Lieber gemeinsam anschauen?') +
      p('Manchmal hilft ein Blick von aussen. In einem Online-Termin von 60 Minuten schauen wir, wo es in deinem Büro hakt. Danach bekommst du einen schriftlichen Plan für die nächsten drei Monate.') +
      p('<strong>CHF&nbsp;330.</strong> Als Toolkit-Käufer rechne ich dir die CHF&nbsp;29 an, du zahlst also CHF&nbsp;301.') +
      btn('Online-Termin wählen', CAL_ON) +
      p(f'Lieber bei dir im Betrieb, mit dem Team? Dann wähl einen <a href="{CAL_VO}" style="color:{PRI};font-weight:700;">Termin vor Ort</a>.', size=14, color=MUTED, mb=16)) +
  p('Und eine Bitte: Was hat dir am Toolkit geholfen, was fehlt? Antworte mit zwei, drei Sätzen auf diese Mail. Ich lese jede Antwort.') +
  p(f'Das war die letzte Mail dieser Reihe. Wenn du weiterhin Tipps möchtest: Einmal im Monat erscheint der <a href="{SITE}/{UTM}#nl" style="color:{PRI};font-weight:700;">Büro-Brief</a>.', mb=24))
open(OUT + 'toolkit-folge-3.html', 'w', encoding='utf-8').write(f3)

# 5) Büro-Brief als Reihe nach der Anmeldung (Brevo-Automation, monatlich, ohne Datumsbezug)
BB = '?utm_source=brevo&utm_medium=email&utm_campaign=buero-brief'
BB_FOOTER = (f'Du erhältst diese E-Mail, weil du dich auf baustelle-buero.ch für den Büro-Brief angemeldet hast.<br>' +
    flinks(('Abmelden', '{{ unsubscribe }}'), ('Im Browser ansehen', '{{ mirror }}'), ('Impressum', SITE + '/#impressum'), ('Datenschutz', SITE + '/#datenschutz')) +
    f'<br><br>{ADDR}')
def a(text, href): return f'<a href="{href}" style="color:{PRI};font-weight:700;">{text}</a>'
def vorlage(title, lines, note='', kick='Zum Abschreiben'):
    body = '<br>'.join(lines)
    return box(kicker(kick) + h2(title) + p(body) + (p(note, size=14, color=MUTED) if note else ''))
TK_LINK = SITE + '/' + BB + '#toolkit'
CHECK_LINK = SITE + '/' + BB
TOOLS_LINK = SITE + '/' + BB + '#werkzeuge'
CAL_ON_BB = 'https://cal.com/baustelle-buero/buero-check-online' + BB
CAL_VO_BB = 'https://cal.com/baustelle-buero/buero-check-vor-ort' + BB
def toolkit_hint(text):
    # Roter Faden zum Toolkit: gleicher Aufbau in jeder Mail, für alle Empfänger gleich.
    return p(f'<strong>Aus dem Toolkit:</strong> {text} Im Toolkit «Ordnung im Betrieb» findest du über 80 Massnahmen, Vorlagen und eine Excel-Arbeitsmappe. ' + a('Toolkit ansehen', TK_LINK), size=14, color=MUTED, mb=16)
def teaser(text):
    return p(f'<strong>Nächsten Monat:</strong> {text}', mb=24)
def next_step(h, text):
    # Mail 6 und 12: zuerst die tiefe Hürde (Toolkit), dann die Beratung.
    return box(kicker('Dein nächster Schritt') + h2(h) + p(text) +
        btn('Toolkit ansehen · CHF 29', TK_LINK) +
        p('Lieber gemeinsam anschauen? In einem ' + a('Online-Termin', CAL_ON_BB) + ' von 60 Minuten gehen wir dein Ergebnis zusammen durch. Mit dem Team bei dir im Betrieb geht es mit einem ' + a('Termin vor Ort', CAL_VO_BB) + '. Preise und Ablauf stehen auf der ' + a('Website', TK_LINK) + '.', size=14, color=MUTED, mb=16))
def brief_nr(nr, title, subject, preheader, inner):
    return shell(subject, preheader, row(kicker(f'Büro-Brief Nr. {nr}') + h1(title) + p(HALLO) + inner + sign(), pad='28px 40px 32px 40px'), BB_FOOTER)
LUECKE = '________'

# Betreff (Posteingang) und Vorschautext je Mail; der Titel in der Mail bleibt sachlich.
BB_META = {
 1: ('Eine Ablage für alles', 'Wo ist die Offerte schon wieder?', 'Ein Ort, sieben Ordner und das Suchen hat ein Ende.'),
 2: ('Ein Name pro Aufgabe', '«Ich dachte, du machst das.»', 'Der Satz, der im Handwerk am meisten Zeit kostet.'),
 3: ('Fünf Fragen vor dem Auftragsstart', 'Die Frage, die bei der Schlussrechnung fehlt', 'Damit die Baustelle weiss, was das Büro weiss.'),
 4: ('Änderungen in vier Teilen', 'Grau statt beige und niemand wusste es', 'Wie eine Änderung zwischen Büro und Baustelle verloren geht.'),
 5: ('Drei Zahlen reichen', 'Drei Zahlen, die dein Bauchgefühl prüfen', 'Kein Controlling. Drei Zahlen, einmal im Monat.'),
 6: ('Zeit für einen zweiten Blick', 'Was hat sich seit dem ersten Check verändert?', 'Fünf Minuten Büro-Check und der Vergleich mit dem letzten Mal.'),
 7: ('Baustellenfotos, die man wiederfindet', 'Wo genau liegt die Leitung?', 'Fünf Fragen zu euren Baustellenfotos. Wie oft sagst du Ja?'),
 8: ('Der Wochenstart in zehn Minuten', 'Was am Montag um 7 Uhr fehlt', 'Drei feste Punkte am Montagmorgen und die Woche läuft ruhiger.'),
 9: ('Rapporte, die stimmen', 'Acht Stunden oder sechs?', 'Fehler erkennen, bevor sie in der Rechnung landen.'),
 10: ('Sag, was du erwartest', 'Die Regel, die nie jemand ausgesprochen hat', 'Eine typische Frage aus der Chefetage und eine ehrliche Antwort.'),
 11: ('Die erste Woche für neue Leute', 'Die erste Woche entscheidet', 'Was Neue in der ersten Woche über eure Abläufe wissen müssen.'),
 12: ('Ein Jahr Büro-Brief', 'Ein Jahr später', 'Was sich in einem Jahr verändert hat und was als Nächstes kommt.'),
}
def bbm(nr, inner):
    t, s, ph = BB_META[nr]
    return brief_nr(nr, t, s, ph, inner)

bb = {}
bb[1] = bbm(1,
  p('Die Offerte steckt in einem Mailanhang, der Plan auf dem Handy des Vorarbeiters, die Fotos auf dem Tablet und die neuste Version auf dem Computer im Büro. Gesucht wird trotzdem jede Woche.') +
  kicker('Tipp') + h2('Leg einen Ort fest, an dem alles landet') +
  p('Wo das ist, spielt eine kleinere Rolle: ein Server im Büro, OneDrive, Google Drive oder Dropbox. Entscheidend ist, dass es nur einen Ort gibt und alle darauf zugreifen können, auch vom Handy aus.') +
  ol(['<strong>Ort bestimmen.</strong> Nimm, was ihr schon habt. Ein Wechsel lohnt sich selten.',
      '<strong>Grundgerüst anlegen.</strong> Wenige Hauptordner reichen, ein Vorschlag steht unten.',
      '<strong>Ab heute alles Neue dort ablegen.</strong> Altes musst du nicht auf einmal umräumen. Verschieb es, wenn du es das nächste Mal brauchst.']) +
  vorlage('Ordnerstruktur für einen Handwerksbetrieb', [
      '<strong>01_Betrieb</strong> (Verträge, Versicherungen, Fahrzeuge, Geräte)',
      '<strong>02_Personal</strong>',
      '<strong>03_Finanzen</strong> (Buchhaltung, Rechnungen, Mahnungen)',
      '<strong>04_Projekte</strong>, pro Auftrag ein Ordner wie <strong>261027_Mueller_Gartenumbau</strong>, darin Offerte, Pläne, Fotos, Rapporte, Rechnung',
      '<strong>05_Lieferanten</strong>',
      '<strong>06_Vorlagen</strong> (Offerte, Rapport, Briefpapier)',
      '<strong>99_Archiv</strong> (abgeschlossene Jahre)'],
      'Die Nummern sorgen dafür, dass die Ordner auf jedem Gerät in der gleichen Reihenfolge erscheinen. Für einheitliche Dateinamen in den Ordnern hilft dir der ' + a('Dateinamen-Generator', TOOLS_LINK) + '.') +
  toolkit_hint('Dieser Tipp stammt aus dem Merkblatt Ablagestruktur.') +
  teaser('der Satz, der im Handwerk am meisten Zeit kostet.'))

bb[2] = bbm(2,
  p('«Ich dachte, du machst das.» Dieser Satz kostet im Handwerk mehr Zeit als jede Software. Material wird doppelt bestellt, eine Offerte bleibt liegen, eine Reklamation wartet eine Woche auf Antwort.') +
  kicker('Tipp') + h2('Schreib zu jeder wiederkehrenden Aufgabe genau einen Namen') +
  p('Gemeint ist nicht die Person, die mithilft, sondern die, die dafür geradesteht. Andere dürfen mitarbeiten, aber eine Person sorgt dafür, dass es erledigt wird.') +
  ol(['<strong>Aufgaben sammeln,</strong> die jede Woche oder jeden Monat anfallen. Fang mit denen an, bei denen es zuletzt gehapert hat.',
      '<strong>Pro Aufgabe einen Namen eintragen</strong> und eine Stellvertretung für Ferien und Krankheit.',
      '<strong>Die Liste aufhängen</strong> oder in den Team-Chat stellen. Sie gilt erst, wenn alle sie gesehen haben.']) +
  vorlage('So sieht das in einem Betrieb mit sechs Leuten aus', [
      '<strong>Offerten nachfassen:</strong> Sandra (Stv. Beat)',
      '<strong>Material bestellen:</strong> Marco (Stv. Luca)',
      '<strong>Rapporte einsammeln:</strong> Sandra (Stv. Marco)',
      '<strong>Rechnungen und Mahnungen:</strong> Beat (Stv. Sandra)',
      '<strong>Reklamationen:</strong> Beat (Stv. Marco)',
      '<strong>Fahrzeuge und Geräte:</strong> Luca (Stv. Marco)'],
      'Mehr braucht es nicht. Ein Blatt Papier am Anschlagbrett reicht.', kick='Beispiel') +
  p('Wie klar die Zuständigkeiten bei euch heute geregelt sind, zeigt dir der ' + a('Büro-Check', CHECK_LINK) + ' in fünf Minuten.') +
  toolkit_hint('Dieser Tipp stammt aus dem Merkblatt Zuständigkeiten. Dazu gibt es eine RACI-Vorlage mit einem ausgefüllten Beispiel.') +
  teaser('die Frage, die bei der Schlussrechnung fehlt.'))

bb[3] = bbm(3,
  p('Im Büro steht alles in der Offerte. Auf der Baustelle kommt davon oft nur ein Teil an: Die Zufahrt ist enger als gedacht, der Kunde wollte doch die andere Platte und niemand wusste, dass der Nachbar informiert werden muss.') +
  kicker('Tipp') + h2('Klär vor jedem Auftrag fünf Fragen, schriftlich') +
  p('Fünf Minuten im Büro sparen auf der Baustelle oft eine Stunde. Wichtig ist, dass die Antworten dort landen, wo das Team sie sieht: im Projektordner oder als Foto im Team-Chat.') +
  vorlage('Übergabe Büro an Baustelle', [
      '<strong>1.</strong> Was genau wird gemacht und was ausdrücklich nicht?',
      '<strong>2.</strong> Wer ist beim Kunden Ansprechperson, mit Telefonnummer?',
      '<strong>3.</strong> Was ist besonders: Zufahrt, Schlüssel, Nachbarn, Tiere, Leitungen?',
      '<strong>4.</strong> Welches Material kommt wann und von wem?',
      '<strong>5.</strong> Was wurde mündlich abgemacht und steht nicht in der Offerte?'],
      'Die fünfte Frage ist die wichtigste. Mündliche Abmachungen sorgen bei der Schlussrechnung oft für Diskussionen.') +
  toolkit_hint('Für diese Übergabe gibt es das ausfüllbare Formular «Auftragsstart», dazu Formulare für Änderungen und für die Rückmeldung ans Büro.') +
  teaser('wie eine Änderung am Telefon auf der Baustelle verloren geht.'))

bb[4] = bbm(4,
  p('Eine Szene, wie sie in vielen Betrieben vorkommt. Wieder im Betrieb mit sechs Leuten, den du schon kennst.') +
  kicker('Dienstag, 16.40 Uhr') +
  p('Frau Keller ruft im Büro an. Die Platten für den Sitzplatz möchte sie doch in Grau statt in Beige. Sandra sagt zu, schreibt es auf einen gelben Zettel und bestellt die grauen Platten nach. Um fünf ist Feierabend.') +
  kicker('Mittwoch, 7.00 Uhr') +
  p('Marco fährt mit Luca auf die Baustelle. Auf dem Platz liegen die beigen Platten, die am Montag geliefert wurden. Die beiden fangen an zu verlegen.') +
  kicker('Mittwoch, 11.30 Uhr') +
  p('Frau Keller schaut vorbei. Ein Drittel der Fläche ist verlegt, in Beige. Jetzt geht es nur noch darum, wer den Rückbau bezahlt.') +
  kicker('Was ist schiefgelaufen?') +
  p('Weder Sandra noch Marco haben etwas falsch gemacht. Die Information hatte einfach keinen festen Weg vom Telefon im Büro bis zur Baustelle.') +
  kicker('Tipp') + h2('Halte jede Änderung fest, immer gleich aufgebaut') +
  p('Dafür brauchst du weder ein Formular noch eine Software. Eine kurze Nachricht im Team-Chat reicht, solange sie immer die gleichen vier Teile hat. Und eine Regel: Wer die Änderung annimmt, schickt die Notiz sofort.') +
  vorlage('Änderungsnotiz', [
      '<strong>Was ändert sich?</strong>',
      '<strong>Wer hat es entschieden?</strong>',
      '<strong>Ab wann gilt es?</strong>',
      '<strong>Wer muss es wissen?</strong>'],
      'So hätte Sandras Nachricht im Team-Chat ausgesehen: Platten Sitzplatz Keller grau statt beige · Kundin am Telefon · ab sofort · Marco und Luca. Was schriftlich festgehalten ist, lässt sich am Schluss auch sauber verrechnen.') +
  toolkit_hint('Für Änderungen gibt es das ausfüllbare Formular «Änderung während der Ausführung».') +
  teaser('drei Zahlen, die dein Bauchgefühl prüfen.'))

bb[5] = bbm(5,
  p('Viele Betriebe entscheiden aus dem Bauch. Das ist nicht falsch, Erfahrung zählt. Aber das Bauchgefühl irrt sich gern bei Fragen wie: Lohnt sich diese Art von Auftrag? Wo geht uns Zeit verloren?') +
  kicker('Tipp') + h2('Schau einmal im Monat auf drei Zahlen') +
  ol(['<strong>Offene Offerten:</strong> Wie viele sind draussen und wie viele davon sind älter als zwei Wochen, ohne dass jemand nachgefragt hat?',
      '<strong>Stunden:</strong> Wie viele Stunden waren kalkuliert, wie viele wurden gebraucht? Zwei, drei abgeschlossene Aufträge reichen.',
      '<strong>Offene Rechnungen:</strong> Welcher Betrag ist mehr als 30 Tage überfällig?']) +
  p('Alle drei Zahlen hast du schon: in der Offertliste, in den Rapporten und in der Buchhaltung. Es geht nur darum, sie regelmässig anzuschauen.') +
  vorlage('Monatsblatt', [
      f'<strong>Monat:</strong> {LUECKE}',
      f'<strong>Offene Offerten:</strong> {LUECKE}, davon älter als zwei Wochen: {LUECKE}',
      f'<strong>Stunden kalkuliert / gebraucht:</strong> {LUECKE} / {LUECKE} (Auftrag: {LUECKE})',
      f'<strong>Überfällige Rechnungen:</strong> CHF {LUECKE}',
      f'<strong>Was mache ich deshalb diesen Monat anders?</strong> {LUECKE}'],
      'Die letzte Zeile ist die wichtigste. Eine Zahl, aus der nichts folgt, ist nur Statistik.') +
  p('Wie stark ihr heute schon mit Zahlen entscheidet, zeigt dir auch der ' + a('Büro-Check', CHECK_LINK) + '.') +
  toolkit_hint('Dieser Tipp stammt aus dem Merkblatt Datenleadership.') +
  teaser('ein zweiter Blick auf euren Stand.'))

bb[6] = bbm(6,
  p('Du bekommst den Büro-Brief jetzt seit einigen Monaten. Zeit für einen Blick zurück: Was hat sich bei euch verändert und was ist liegen geblieben?') +
  kicker('Tipp') + h2('Mach den Büro-Check noch einmal') +
  p('Er dauert fünf Minuten. Wenn du das Ergebnis mit «Im Verlauf speichern» sicherst, zeigt dir die Seite «Verlauf» den Vergleich mit dem letzten Mal. Das klappt auf dem gleichen Gerät im gleichen Browser, denn deine Antworten bleiben bei dir und werden nicht übertragen.') +
  btn('Büro-Check starten', CHECK_LINK) +
  h2('So nutzt du das Ergebnis') +
  ol(['<strong>Schau, was besser geworden ist</strong> und sag es dem Team. Fortschritt, den niemand bemerkt, motiviert niemanden.',
      '<strong>Wähl einen Bereich, der stehen geblieben ist</strong> und nimm dir dafür genau eine Massnahme vor.',
      '<strong>Trag den nächsten Check in den Kalender,</strong> in drei Monaten.']) +
  next_step('Die Lücke schliessen',
      'Der Büro-Check zeigt dir, wo es hakt. Das Toolkit «Ordnung im Betrieb» zeigt dir für jeden Bereich, wie du es mit dem Team umsetzt: Merkblätter mit über 80 Massnahmen, Vorlagen, Übergabeformulare und eine Excel-Arbeitsmappe, die eure Fortschritte festhält.') +
  teaser('wo genau die Leitung liegt. Und warum das Handy darauf keine Antwort hat.'))

bb[7] = bbm(7,
  p('Auf jedem Handy im Betrieb liegen Hunderte von Baustellenfotos. Wenn der Kunde zwei Jahre später fragt, wo genau die Leitung durchgeht, beginnt die Suche: Wer war damals dort? Hat er das Handy noch?') +
  kicker('Selbsttest') + h2('Fünf Fragen, ehrlich beantwortet') +
  p('Zähl, wie oft du Ja sagen kannst.') +
  ol(['Findest du die Fotos eines Auftrags vom letzten Jahr in weniger als zwei Minuten?',
      'Liegen die Baustellenfotos an einem Ort, auf den auch das Büro Zugriff hat?',
      'Gibt es von jedem grösseren Auftrag Fotos vom Zustand vor Arbeitsbeginn?',
      'Werden Leitungen vor dem Zudecken fotografiert, mit Massband im Bild?',
      'Weiss jemand im Team, dass er für das Hochladen zuständig ist?']) +
  p('<strong>Fünfmal Ja:</strong> Das läuft bei euch. <strong>Drei- oder viermal:</strong> Die Grundlage steht, es fehlt eine feste Regel. <strong>Zweimal oder weniger:</strong> Dann lohnt sich der Tipp unten besonders.') +
  kicker('Tipp') + h2('Leg Fotos im Projektordner ab, nicht nur auf dem Handy') +
  ol(['<strong>Pro Auftrag einen Ordner «Fotos» anlegen,</strong> im Projektordner. Mit einer Cloud-Ablage kann das Team direkt vom Handy hochladen.',
      '<strong>Einmal pro Woche hochladen,</strong> am besten am Freitag vor Feierabend. Wer daran erinnert, steht auf der Zuständigkeitsliste.',
      '<strong>Nur wichtige Fotos umbenennen.</strong> Für einheitliche Namen hilft der ' + a('Dateinamen-Generator', TOOLS_LINK) + '. Der Rest darf bleiben, wie er ist.']) +
  vorlage('Diese Fotos immer machen', [
      '<strong>Vorher:</strong> Zustand bei Arbeitsbeginn, auch bestehende Schäden',
      '<strong>Vor dem Zudecken:</strong> Leitungen, Rohre, Armierungen und Abdichtungen, mit Massband im Bild',
      '<strong>Bei Änderungen:</strong> was anders gemacht wurde als geplant',
      '<strong>Nachher:</strong> das fertige Werk aus den gleichen Blickwinkeln wie vorher'],
      'Fotos von bestehenden Schäden ersparen dir später manche Diskussion darüber, wer was verursacht hat.') +
  toolkit_hint('Dieser Tipp stammt aus dem Merkblatt Ablagestruktur.') +
  teaser('was am Montag um 7 Uhr fehlt.'))

bb[8] = bbm(8,
  p('Am Montagmorgen fährt jeder auf seine Baustelle. Was das Büro über die Woche weiss, erfährt das Team oft erst, wenn es zu spät ist: Der Kunde ist am Donnerstag nicht da, das Material kommt einen Tag später, der Bagger ist doppelt verplant.') +
  kicker('Tipp') + h2('Steht am Montag zehn Minuten zusammen, immer mit den gleichen drei Punkten') +
  p('Ohne Sitzungszimmer und ohne Präsentation: im Werkhof, im Büro oder per Videoanruf, im Stehen. Wichtig ist, dass der Wochenstart jede Woche stattfindet und nie länger als zehn Minuten dauert.') +
  vorlage('Wochenstart in drei Punkten', [
      '<strong>1. Was läuft diese Woche?</strong> Baustellen, Termine, wer ist wo.',
      '<strong>2. Was hat sich geändert?</strong> Neue Abmachungen, verschobene Lieferungen, Abwesenheiten.',
      '<strong>3. Wo klemmt es?</strong> Fehlende Infos, fehlendes Material, offene Entscheide. Hier nur benennen, gelöst wird später.'],
      'Beim dritten Punkt kommt das Wichtigste auf den Tisch. Halte fest, wer sich bis wann darum kümmert.') +
  p('Mit mehreren Equipen reicht es, wenn die Vorarbeiter dabei sind. Sie geben die Infos danach an ihr Team weiter.') +
  toolkit_hint('Dieser Tipp stammt aus dem Merkblatt Datenleadership.') +
  teaser('acht Stunden oder sechs? Wie Rapporte stimmen, bevor die Rechnung rausgeht.'))

bb[9] = bbm(9,
  p('Der Rapport sagt acht Stunden, die Arbeit war nach sechs fertig. Oder umgekehrt: Zwei Stunden Aufräumen fehlen, weil niemand daran gedacht hat. Solche Fehler fallen meist erst bei der Rechnung auf. Im schlechtesten Fall bemerkt sie der Kunde.') +
  kicker('Tipp') + h2('Prüf jeden Rapport kurz, bevor er abgelegt wird') +
  p('Es geht nicht um Misstrauen. Rapporte entstehen meist am Abend, müde und aus dem Gedächtnis. Ein kurzer Blick am nächsten Tag findet die meisten Fehler.') +
  vorlage('Drei Prüffragen für jeden Rapport', [
      '<strong>Passt es zusammen?</strong> Stimmen Stunden, Personen und Datum mit dem Einsatzplan überein?',
      '<strong>Ist es vollständig?</strong> Sind Material, Maschinen, Fahrten und Mehraufwand eingetragen?',
      '<strong>Ist es plausibel?</strong> Würde jemand anderes für die gleiche Arbeit ungefähr gleich lange brauchen?'],
      'Wenn etwas nicht stimmt: nicht selbst korrigieren, sondern nachfragen. So lernt das Team, worauf es ankommt.') +
  p('Dazu eine Gewohnheit: Sprich Fehler, die mehrmals vorkommen, einmal im Monat im Team an, ohne Namen. Meist liegt es am Formular oder an einer unklaren Regel und nicht an der Person.') +
  toolkit_hint('Dieser Tipp stammt aus dem Merkblatt Datenkompetenz. Dazu kommt das Formular «Rückmeldung ans Büro», mit dem die Baustelle Mehraufwand gleich festhält.') +
  teaser('die Regel, die nie jemand ausgesprochen hat.'))

bb[10] = bbm(10,
  kicker('Eine typische Frage') +
  p('<strong>«Ich habe dem Team doch gesagt, dass alles in den Projektordner gehört. Warum hält sich keiner daran?»</strong>') +
  kicker('Die ehrliche Antwort') +
  p('Weil ein Satz in einer Sitzung keine Regel ist. Eine Regel wird es erst, wenn sie aufgeschrieben ist, wenn die Führung sie selbst einhält und wenn jemand nachfragt, sobald sie nicht eingehalten wird. Fehlt einer dieser drei Teile, gilt im Alltag wieder die alte Gewohnheit.') +
  p('Das ist kein Vorwurf ans Team. In vielen Betrieben gelten Regeln, die nie jemand ausgesprochen hat. Die neue Mitarbeiterin legt Dateien auf dem Desktop ab. Der Vorarbeiter schickt Baustellenfotos nur in seinen privaten Chat. Niemand sagt etwas, denn niemand hat je gesagt, wie es sein soll.') +
  kicker('Tipp') + h2('Schreib fünf Regeln auf und sprich sie aus') +
  vorlage('Fünf Regeln für den Umgang mit Daten', [
      '<strong>1.</strong> Alles, was zu einem Auftrag gehört, kommt in den Projektordner.',
      '<strong>2.</strong> Dateien bekommen einen Namen nach unserem Muster.',
      '<strong>3.</strong> Änderungen geben wir sofort schriftlich weiter.',
      '<strong>4.</strong> Rapporte sind am nächsten Morgen im Büro.',
      '<strong>5.</strong> Wer einen Fehler bemerkt, meldet ihn. Es geht um die Sache und nicht um Schuld.'],
      'Nimm die Beispiele als Startpunkt und pass sie an euren Betrieb an. Fünf Regeln, die gelten, sind mehr wert als zwanzig auf Papier.') +
  h2('So führst du sie ein') +
  ol(['<strong>In der nächsten Teamsitzung vorstellen</strong> und begründen: Warum ist uns das wichtig?',
      '<strong>Selbst vorleben.</strong> Wenn die Chefin ihre eigenen Dateien sauber ablegt, zieht das Team viel eher mit.',
      '<strong>Nach einem Monat nachfragen:</strong> Was klappt, was nicht? Regeln, die nicht funktionieren, darfst du ändern.']) +
  toolkit_hint('Dieser Tipp stammt aus dem Merkblatt Datenleadership.') +
  teaser('warum die erste Woche von neuen Leuten so viel entscheidet.'))

bb[11] = bbm(11,
  p('Neue Mitarbeitende lernen schnell, wie man auf der Baustelle arbeitet. Wo etwas abgelegt wird, wie ein Rapport aussieht und wer wofür zuständig ist, lernen sie dagegen oft nur nebenbei. Nach ein paar Monaten hat jeder sein eigenes System.') +
  kicker('Tipp') + h2('Erklär in der ersten Woche nicht nur das Wie, sondern auch das Warum') +
  p('Wer versteht, warum es eine Regel gibt, hält sich eher daran. «Fotos kommen in den Projektordner, damit wir bei einer Reklamation in zwei Jahren noch etwas belegen können» wirkt mehr als «Fotos kommen in den Projektordner».') +
  vorlage('Checkliste für die erste Woche', [
      '<strong>Zugänge:</strong> Ablage, Mail, Team-Chat und Zeiterfassung funktionieren, auch auf dem Handy.',
      '<strong>Ablage:</strong> Ordnerstruktur und Dateinamen gezeigt, einmal selbst etwas abgelegt.',
      '<strong>Rapport:</strong> einen Rapport gemeinsam ausgefüllt und besprochen.',
      '<strong>Zuständigkeiten:</strong> Liste gezeigt. Wen frage ich bei Material, Plänen oder Ferien?',
      '<strong>Regeln:</strong> die wichtigsten Regeln erklärt, jeweils mit dem Warum.',
      '<strong>Ansprechperson:</strong> eine Person bestimmt, die in den ersten Wochen Fragen beantwortet.'],
      'Die Liste hilft auch bei Lernenden, Temporären und Saisonkräften.') +
  toolkit_hint('Dieser Tipp stammt aus dem Merkblatt Datenkompetenz.') +
  teaser('der Jahres-Check. Was ist nach einem Jahr wirklich anders?'))

bb[12] = bbm(12,
  p('Seit bald einem Jahr bekommst du den Büro-Brief: elf Tipps zu Ablage, Zuständigkeiten, Übergaben, Zahlen und Führung. Danke, dass du dabeigeblieben bist.') +
  kicker('Tipp') + h2('Mach den Jahres-Check') +
  p('Nimm dir eine Stunde Zeit und geh drei Fragen durch, allein oder mit dem Team.') +
  vorlage('Jahres-Check in drei Fragen', [
      '<strong>1. Was ist heute besser als vor einem Jahr?</strong> Schreib mindestens drei Dinge auf, auch kleine.',
      '<strong>2. Was haben wir angefangen und nicht durchgezogen?</strong> Weiterführen oder bewusst streichen?',
      '<strong>3. Was nehmen wir uns für die nächsten drei Monate vor?</strong> Höchstens zwei Dinge, mit Namen und Datum.']) +
  p('Mach dazu den Büro-Check noch einmal. Wenn du deine Ergebnisse im Verlauf gespeichert hast, siehst du die Entwicklung auf einen Blick.') +
  btn('Büro-Check starten', CHECK_LINK) +
  next_step('Das nächste Jahr planen',
      'Für die nächsten Schritte gibt es zwei Wege. Selbst umsetzen mit dem Toolkit «Ordnung im Betrieb»: über 80 Massnahmen, Vorlagen und eine Excel-Arbeitsmappe. Oder gemeinsam planen in einem Termin.') +
  p('Der Büro-Brief geht weiter, mit neuen Themen und Neuigkeiten von baustelle-büro.', mb=24))

for nr, html in bb.items():
    open(OUT + f'buero-brief-{nr}.html', 'w', encoding='utf-8').write(html)
print('ok')
