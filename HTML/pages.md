# HTML Routes and Pages

## Understanding Routes in HTML

In web development, a route typically refers to a URL pattern that is associated with a particular page or content on a website. When a user navigates to a specific route, the server or client-side application delivers the corresponding page.

### Default Route (`/`)
- The default route (`/`) is the base route of a website. When you navigate to the root of a domain (e.g., `https://example.com/`), it typically displays the homepage.
- **Example**:
  ```html
  <a href="/">Home</a>
  ```

### Nested Routes
- Example: `/services/web-development`
  ```html
  <a href="/services/web-development">Web Development</a>
  ```

This link navigates to a more specific section under the services page, such as a dedicated page for web development services.

### Query Parameters
Query parameters can be added to routes to pass additional information. They are typically used for filtering or sorting content on a page.
- **Example**:
  ```html
  <a href="/search?query=html">Search for HTML</a>
  ```

This link directs to a search results page that displays results related to the query "HTML".

### Hash Routing
Hash routes are used for navigating to specific sections within the same page.
- **Example**:
  ```html
  <a href="/about#team">Meet the Team</a>
  ```

### Best Practices for Structuring Routes
- **Consistency**: Keep your route names consistent. For example, if you use `/about-us`, stick with similar patterns like `/contact-us`.
- **Readability**: Use lowercase letters and hyphens to separate words. Avoid spaces and underscores.
- **Meaningful Names**: Make sure each route clearly represents the content it leads to, making navigation intuitive for users.

### HTML Example of a Simple Website Navigation
```html
<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About Us</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</nav>
```