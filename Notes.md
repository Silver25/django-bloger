### IMG Accordion (collapsible content)
<details>
<summary>Responsive visual <b style="color: yellow;">(open here)</b></summary>  
<!-- Change code from ![Wireframe for site](assets/documentation/wireframe01.webp) -->
<img src="assets/documentation/intro-responsive2.webp">
</details>
  

![Description for image](readme-assets/image13.png)  

- descriptive line as a bullet point
  
---
---

### last modifications
- xxx

---
---

**python manage.py runserver**  
**DEBUG: False, git add, commit and push**
  
  
### REGENERATE the 'SECRET_KEY' [settings.py] for final production deployment
- Terminal: **python -c 'import secrets; print(secrets.token_urlsafe(40))'**  [ prints lower, upper, numerical & special char ]
or  
- Terminal: **python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'**
