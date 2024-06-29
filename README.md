## Flask Application Design

### HTML Files

1. **home.html:**
   - Contains the layout and content for the home page, including the video banner, mission statement, and call to action.
2. **solutions.html:**
   - Provides details about geothermal energy solutions, case studies, and a request quote button.
3. **news.html:**
   - Displays a list of news articles with social sharing buttons.
4. **about_us.html:**
   - Introduces the company, its history, values, and team.
5. **contact_us.html:**
   - Features a contact form, contact details, and a map.

### Routes

**Homepage:**
- `/`: Renders the home page (`home.html`).

**Solutions:**
- `/solutions`: Renders the solutions page (`solutions.html`).

**News:**
- `/news`: Renders the news page (`news.html`).

**About Us:**
- `/about-us`: Renders the about us page (`about_us.html`).

**Contact Us:**
- `/contact-us`: Renders the contact us page (`contact_us.html`).

**Additional Routes:**
- `/media/video.mp4`: Serves the MP4 video for the home page banner.
- Static routes for CSS, JavaScript, and images.