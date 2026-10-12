SHIVAAY SMM — DEMO STARTER

इस पैकेज में:
- index.html: मोबाइल-फ्रेंडली वेबसाइट डेमो, कैटलॉग और नकली/स्थानीय demo orders
- bot.py: Telegram bot starter
- requirements.txt: Python dependency

महत्वपूर्ण:
यह अभी केवल डेमो है। वेबसाइट किसी सर्वर/डेटाबेस से जुड़ी नहीं है। पेमेंट, UPI, supplier API, wallet या असली ऑर्डर प्रोसेसिंग नहीं होती। डेमो कीमतें वास्तविक सप्लायर रेट नहीं हैं।

iPhone पर वेबसाइट डेमो:
1. ZIP को Files app में खोलें और index.html को उपलब्ध HTML preview/browser विकल्प से देखें। यदि preview नहीं खुलता, किसी HTML preview app या कंप्यूटर का उपयोग करें।
2. वेबसाइट को public/live करने के लिए hosting पर upload करना होगा; यह ZIP अपने-आप इंटरनेट पर प्रकाशित नहीं है।

Telegram bot (कंप्यूटर या cloud server पर):
1. Python 3.10+ इंस्टॉल करें।
2. Terminal में इस फ़ोल्डर में जाएँ और चलाएँ: pip install -r requirements.txt
3. BotFather से token लें। Token निजी रखें।
4. Environment variable सेट करें:
   macOS/Linux: export TELEGRAM_BOT_TOKEN='YOUR_TOKEN'
   Windows PowerShell: $env:TELEGRAM_BOT_TOKEN='YOUR_TOKEN'
5. चलाएँ: python bot.py

iPhone-only नोट:
बॉट को लगातार चलाने के लिए cloud hosting या ऐसा service चाहिए जो Python process चलाए। सिर्फ Telegram ऐप से Python bot लगातार नहीं चलता।

अगला production चरण:
- backend API + PostgreSQL database
- सुरक्षित admin login और role checks
- order validation, rate limits, logs, backups
- UPI/payment gateway merchant onboarding और server-side payment verification
- सेवा प्रदाता API की जाँच, terms compliance, refunds और customer support
- वास्तविक पेमेंट या ग्राहक डेटा जोड़ने से पहले security review
