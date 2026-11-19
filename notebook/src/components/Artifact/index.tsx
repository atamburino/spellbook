import React, {useState, useEffect} from 'react';

interface ArtifactProps {
  /** Raw HTML string to render in a sandboxed iframe */
  html: string;
  /** Height of the iframe in pixels */
  height?: number;
  /** Title for accessibility */
  title?: string;
}

/**
 * Renders arbitrary HTML/CSS/JS in a sandboxed iframe.
 * Use this for Claude-artifact-style interactive components.
 *
 * Usage in MDX:
 *
 * ```mdx
 * import Artifact from '@site/src/components/Artifact';
 *
 * <Artifact
 *   title="Interactive counter"
 *   height={300}
 *   html={`
 *     <!DOCTYPE html>
 *     <html>
 *     <body>
 *       <button onclick="document.getElementById('count').textContent = ++window.c">
 *         Click me
 *       </button>
 *       <p>Count: <span id="count">0</span></p>
 *       <script>window.c = 0;</script>
 *     </body>
 *     </html>
 *   `}
 * />
 * ```
 */
export default function Artifact({html, height = 400, title = 'Interactive artifact'}: ArtifactProps) {
  const [srcDoc, setSrcDoc] = useState('');

  useEffect(() => {
    // Inject a base style reset so artifacts look clean
    const styled = html.includes('<style') || html.includes('<link')
      ? html
      : `
        <style>
          *, *::before, *::after { box-sizing: border-box; }
          body {
            margin: 0;
            padding: 16px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #e4e4e7;
            background: #18181b;
          }
        </style>
        ${html}
      `;
    setSrcDoc(styled);
  }, [html]);

  return (
    <div style={{
      border: '1px solid #3f3f46',
      borderRadius: '8px',
      overflow: 'hidden',
      margin: '16px 0',
    }}>
      <div style={{
        background: '#27272a',
        padding: '6px 12px',
        fontSize: '12px',
        color: '#a1a1aa',
        borderBottom: '1px solid #3f3f46',
        display: 'flex',
        alignItems: 'center',
        gap: '6px',
      }}>
        <span>⚡</span>
        <span>{title}</span>
      </div>
      <iframe
        srcDoc={srcDoc}
        title={title}
        sandbox="allow-scripts"
        style={{
          width: '100%',
          height: `${height}px`,
          border: 'none',
          background: '#18181b',
        }}
      />
    </div>
  );
}
