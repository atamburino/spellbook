import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Spellbook',
  tagline: 'A unified reference notebook',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://atamburino.github.io',
  baseUrl: '/spellbook/',

  organizationName: 'atamburino',
  projectName: 'spellbook',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'log',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/', // Docs at root — no /docs/ prefix
          editUrl: 'https://github.com/atamburino/spellbook/edit/main/notebook/',
          showLastUpdateTime: true,
        },
        blog: false, // We're a notebook, not a blog
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: ['@docusaurus/theme-live-codeblock'],

  themeConfig: {
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: '📖 Spellbook',
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'referencesSidebar',
          position: 'left',
          label: 'References',
        },
        {
          type: 'docSidebar',
          sidebarId: 'schoolSidebar',
          position: 'left',
          label: 'School',
        },
        {
          type: 'search',
          position: 'right',
        },
        {
          href: 'https://github.com/atamburino/spellbook',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Spellbook · Andy Tamburino · ${new Date().getFullYear()}`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['lua', 'bash', 'powershell', 'json', 'sql', 'python', 'ruby'],
    },
    tableOfContents: {
      minHeadingLevel: 2,
      maxHeadingLevel: 4,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
