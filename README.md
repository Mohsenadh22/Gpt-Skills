# Gpt-Skills

مجموعهٔ ۱۸ مهارت برای طراحی، ساخت، بررسی و انتشار سایت با Codex.
هر مهارت با فایل‌های کمکی و منابع خودش نگهداری می‌شود. نسخهٔ دقیق منبع و
اثر انگشت فایل‌ها در [sources.lock.json](sources.lock.json) ثبت شده است.

## مهارت‌ها

| مهارت / پوشه | کاربرد | منبع |
| --- | --- | --- |
| [frontend-design](.agents/skills/frontend-design/SKILL.md) | طراحی ظاهر سایت، لندینگ و داشبورد | Anthropic |
| [react-best-practices](.agents/skills/react-best-practices/SKILL.md) | کیفیت و کارایی React و Next.js | Vercel |
| [web-design-guidelines](.agents/skills/web-design-guidelines/SKILL.md) | تجربه کاربری، دسترس‌پذیری و فرم‌ها | Vercel |
| [composition-patterns](.agents/skills/composition-patterns/SKILL.md) | ساخت اجزای قابل‌استفاده مجدد React | Vercel |
| [playwright](.agents/skills/playwright/SKILL.md) | بررسی مسیرهای کاربر در مرورگر واقعی | OpenAI |
| [webapp-testing](.agents/skills/webapp-testing/SKILL.md) | تست عملکرد وب‌اپ | Anthropic |
| [security-best-practices](.agents/skills/security-best-practices/SKILL.md) | بررسی امنیت کد | OpenAI |
| [seo-audit](.agents/skills/seo-audit/SKILL.md) | بررسی سئوی فنی و صفحات | Corey Haines |
| [figma-implement-design](.agents/skills/figma-implement-design/SKILL.md) | تبدیل طرح Figma به کد | OpenAI |
| [security-threat-model](.agents/skills/security-threat-model/SKILL.md) | بررسی تهدیدهای معماری سایت | OpenAI |
| [gh-fix-ci](.agents/skills/gh-fix-ci/SKILL.md) | رفع خطاهای GitHub Actions | OpenAI |
| [gh-address-comments](.agents/skills/gh-address-comments/SKILL.md) | رسیدگی به نظرات بازبینی کد | OpenAI |
| [sentry](.agents/skills/sentry/SKILL.md) | بررسی خطاهای ثبت‌شده در Sentry | OpenAI |
| [aspnet-core](.agents/skills/aspnet-core/SKILL.md) | ساخت سایت و سرویس با .NET | OpenAI |
| [vercel-deploy](.agents/skills/vercel-deploy/SKILL.md) | انتشار روی Vercel | OpenAI |
| [cloudflare-deploy](.agents/skills/cloudflare-deploy/SKILL.md) | انتشار روی Cloudflare | OpenAI |
| [netlify-deploy](.agents/skills/netlify-deploy/SKILL.md) | انتشار روی Netlify | OpenAI |
| [render-deploy](.agents/skills/render-deploy/SKILL.md) | انتشار روی Render | OpenAI |

نام داخلی بعضی مهارت‌های Vercel در `SKILL.md` با نام پوشه متفاوت است.
اسکریپت نصب از نام داخلی معتبر استفاده می‌کند.

## استفاده در Codex

مهارت‌ها در `.agents/skills/` هستند تا هنگام کار در همین مخزن شناسایی شوند.
[AGENTS.md](AGENTS.md) توضیح می‌دهد برای هر کار از کدام مهارت استفاده شود.

برای استفاده در پروژه‌های دیگر، مخزن را دریافت کن و نصب محلی را اجرا کن:

```powershell
git clone https://github.com/Mohsenadh22/Gpt-Skills.git
cd Gpt-Skills
python scripts/verify_collection.py
python scripts/install_local.py --dry-run
python scripts/install_local.py
```

مهارت‌ها در پوشهٔ `skills` زیر `CODEX_HOME`، یا به‌صورت پیش‌فرض در
`~/.codex/skills` نصب می‌شوند و از نوبت بعدی Codex در دسترس قرار می‌گیرند.
فایل موجود با محتوای متفاوت بازنویسی نمی‌شود.

این مهارت‌ها مستقل از اتصال حساب سرویس‌ها هستند. استفاده از Figma، Sentry و
سرویس انتشار به ابزار و دسترسی حساب مربوطه نیاز دارد. Supabase یک افزونهٔ
جداگانه است و جزو این ۱۸ مهارت نیست. وابستگی‌های اجرایی هر مهارت در فایل
`SKILL.md` آن توضیح داده شده‌اند؛ برخی ابزارهای کمکی به Bash، Node.js یا Python
نیاز دارند.

## منابع و مجوزها

منابع اصلی: [OpenAI](https://github.com/openai/skills)،
[Anthropic](https://github.com/anthropics/skills)،
[Vercel](https://github.com/vercel-labs/agent-skills) و
[Corey Haines](https://github.com/coreyhaines31/marketingskills).

فایل‌های بالادستی بدون تغییر وارد شده‌اند. مجوز هر مهارت و فایل مربوطه بر آن
حاکم است؛ [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) و پوشهٔ
[licenses](licenses/) جزئیات را نگه می‌دارند.
