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
     p(f'Mit dem Klick willigst du ein, dass wir dir den Büro-Brief alle zwei Wochen per E-Mail schicken. Du kannst ihn jederzeit mit einem Klick abbestellen. Mehr dazu in der <a href="{SITE}/#datenschutz" style="color:{PRI};">Datenschutzerklärung</a>.', size=14, color=MUTED) +
     p('Du hast dich nicht angemeldet? Dann ignoriere diese E-Mail einfach. Ohne Bestätigung erhältst du keine weiteren Nachrichten.', size=14, color=MUTED, mb=24) +
     sign(), pad='28px 40px 32px 40px'),
 f'{ADDR}<br>' + flinks(('baustelle-buero.ch', SITE), ('Impressum', SITE + '/#impressum'), ('Datenschutz', SITE + '/#datenschutz')))
open(OUT + 'double-opt-in.html', 'w', encoding='utf-8').write(doi)

# 2) Willkommen (finale Bestätigung)
welcome = shell('Willkommen beim Büro-Brief', 'Das erwartet dich, und ein erster Tipp für heute.',
 row(kicker('Büro-Brief') + h1('Schön, dass du dabei bist') +
     p('Ich bin Florian, Gärtner HF mit IT-Hintergrund. In meiner Diplomarbeit habe ich untersucht, wie Handwerksbetriebe mit ihren Daten umgehen. Daraus ist baustelle-büro entstanden: weniger Büro nach Feierabend.') +
     h2('Was dich erwartet') +
     ul(['Alle zwei Wochen ein Tipp, den du in 15 Minuten umsetzen kannst', 'Vorlagen, die du direkt im Betrieb brauchen kannst', 'Kein Fachchinesisch und keine Werbeflut']) +
     '<!-- PLATZ FÜR GRATIS-VORLAGE: Sobald die Ordnerstruktur bereit ist, hier eine Box mit Download-Button einfügen. -->\n' +
     box(kicker('Dein erster Tipp') + h2('Dateinamen, die man wiederfindet') +
         p('Benenne jede Datei nach dem gleichen Muster: Datum, Projekt, Inhalt, Version. Zum Beispiel <strong>261027_Gartenumbau-Mueller_Offerte_v1.pdf</strong>. So findest du jede Datei in Sekunden, auch die vom letzten Jahr.') +
         btn('Zum Dateinamen-Generator', SITE + '/#werkzeuge')) +
     p(f'Noch nicht gemacht? Der <a href="{SITE}" style="color:{PRI};font-weight:700;">Büro-Check</a> zeigt dir in fünf Minuten, wo dein Betrieb steht.') +
     p('Und eine Bitte: Antworte kurz auf diese E-Mail und schreib mir, was dich im Büro am meisten nervt. Ich lese jede Antwort, und die besten Fragen beantworte ich im Büro-Brief.', mb=24) +
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
print('ok')
