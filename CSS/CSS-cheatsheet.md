# CSS Cheatsheet

## Selectors

Selectors specify the HTML elements you want to style. In CSS, they can be simple or complex.

- **Universal Selector (`*`)**: Selects all elements.
- **Type Selector (`element`)**: Selects all elements of a given type.
- **Class Selector (`.class`)**: Selects all elements with a given class.
- **ID Selector (`#id`)**: Selects the element with a specific ID.
- **Attribute Selector (`[attribute]`)**: Selects elements with a specific attribute.
- **Pseudo-class Selector (`:pseudo-class`)**: Selects elements based on their state.
- **Pseudo-element Selector (`::pseudo-element`)**: Selects a part of an element.

Example:

```css
p {
  color: blue;
}
```

## Declaration Block

The declaration block is everything inside the curly braces `{}` in a CSS rule. It contains one or more declarations, each specifying a CSS property and value.

- **Declaration**: A single property-value pair in CSS. Example: `color: red;`
- **Property**: The style attribute you want to change (e.g., `color`, `font-size`).
- **Value**: The value assigned to the property (e.g., `red`, `16px`).
  Example:

```css
selector {
  property: value; /* Declaration */
}
```

## Syntax Components

- **Delimiter (`;`)**: Used to separate declarations within a declaration block. Best practice is to always include it, even after the last declaration.
- **Colon (`:`)**: Used to separate the property from its value in a declaration.
- **Curly Braces (`{}`)**: Used to contain the declaration block associated with a selector.

## Example

```css
.selector {
  color: blue; /* Declaration */
  font-size: 16px;
}
```

### Pseudo-Classes and Pseudo-Elements

- **Pseudo-Class:** A keyword added to a selector that specifies a special state of the selected elements (e.g., `:hover`, `:focus`).
- **Pseudo-Element:** A keyword added to a selector that styles a specific part of the selected element (e.g., `::before`, `::after`).

## Best Practices

- Always include a semicolon (`;`) after each declaration.
- Use meaningful class and ID names.
- Keep your CSS organized and modular by grouping related styles together.
