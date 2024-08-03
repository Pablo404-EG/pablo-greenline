# pablo-greenline
### WA_PROTECTOR

WA_PROTECTOR هو سكريبت لحماية رقم الواتساب الخاص بك من خلال حظر جهات الاتصال غير المعروفة تلقائيًا.

## التثبيت

1. تحديث النظام وتثبيت الحزم الضرورية:

    ```sh
    apt update && apt upgrade -y
    pkg install python git -y
    pip install colorama selenium
    pkg install chromium
    ```

2. استنساخ المستودع:

    ```sh
    git clone https://github.com/Pablo404-EG/pablo-greenline
.git
    cd WA_PROTECTOR
    ```

3. تشغيل السكريبت:

    ```sh
    python WA_PROTECTOR.py
    ```

4. اتبع التعليمات الظاهرة على الشاشة لمسح رمز QR الخاص بـ WhatsApp Web ودع السكريبت يراقب الرسائل ويحظر جهات الاتصال غير المعروفة تلقائيًا.

## الاستخدام

- سيقوم السكريبت بجلب جهات الاتصال المعروفة من WhatsApp Web بعد مسح رمز QR.
- ثم سيقوم بمراقبة الرسائل الواردة وحظر أي جهات اتصال غير معروفة تلقائيًا.
