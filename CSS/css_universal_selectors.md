# Universal Selectors in CSS

In CSS, universal selectors are used to target all elements within a document. Here are the key universal selectors and how they work:

## 1. Universal Selector (`*`)
- Targets every element on the page.
- **Example:**
    ```css
    * {
      margin: 0;
      padding: 0;
    }
    ```
- This resets the margin and padding for all elements.

## 2. Attribute Selector (`[attr]`)
- Targets elements that have a specific attribute, regardless of its value.
- **Example:**
    ```css
    [title] {
      color: blue;
    }
    ```
- This will style all elements with a `title` attribute.

## 3. Attribute Value Selector (`[attr=value]`)
- Targets elements with a specific attribute and value.
- **Example:**
    ```css
    [type="text"] {
      border: 1px solid #ccc;
    }
    ```
- This styles all input elements with `type="text"`.

## 4. Grouped Selector (`,`)
- Targets multiple elements grouped together.
- **Example:**
    ```css
    h1, h2, h3 {
      font-family: Arial, sans-serif;
    }
    ```
- This applies the same styles to `h1`, `h2`, and `h3`.

## 5. Child Selector (`>`)
- Targets direct child elements.
- **Example:**
    ```css
    div > p {
      color: red;
    }
    ```
- This targets all `p` elements that are direct children of a `div`.

## 6. Descendant Selector (` `)
- Targets all descendants of a particular element.
- **Example:**
    ```css
    div p {
      color: green;
    }
    ```
- This targets all `p` elements inside a `div`, no matter how deeply nested.

## 7. Pseudo-Class Selectors (`:pseudo-class`)
- Targets elements based on their state or position.
- **Example:**
    ```css
    a:hover {
      color: orange;
    }
    ```
- This changes the color of a link when it is hovered over.

## 8. Pseudo-Element Selectors (`::pseudo-element`)
- Targets specific parts of an element.
- **Example:**
    ```css
    p::first-line {
      font-weight: bold;
    }
    ```
- This targets and styles the first line of a paragraph.

## 9. Atomizing (`.hidden`)
- **Example:**
    ```css
    hidden {
      display: none;
    }
    ```
- We can create classes that we can leverage as conditonal on state.

These selectors can be combined in various ways to create more specific and powerful styles.
