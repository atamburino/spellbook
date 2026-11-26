import React, {type ReactNode} from 'react';
import Link from '@docusaurus/Link';
import {useCurrentSidebarCategory} from '@docusaurus/plugin-content-docs/client';
import type {
  PropSidebarItem,
  PropSidebarItemCategory,
} from '@docusaurus/plugin-content-docs';

import styles from './styles.module.css';

type PageLink = {
  href: string;
  label: string;
};

type ClassCard = {
  href: string;
  code?: string;
  name: string;
  description: string;
  pages: PageLink[];
};

const courseCode = /^([A-Z]{2,}-\d+)\s+(.+)$/;
const quickLinkPreference = [/glossary/i, /python patterns/i];

function pagesOf(item: PropSidebarItem): PageLink[] {
  if (item.type === 'link') {
    return [{href: item.href, label: item.label}];
  }
  if (item.type !== 'category') {
    return [];
  }
  const pages: PageLink[] = [];
  if (item.href) {
    pages.push({href: item.href, label: 'Overview'});
  }
  for (const child of item.items) {
    if (child.type === 'link' && child.href !== item.href) {
      pages.push({href: child.href, label: child.label});
    } else if (child.type === 'category' && child.href) {
      pages.push({href: child.href, label: child.label});
    }
  }
  return pages;
}

function splitCourse(label: string): {code?: string; name: string} {
  const match = label.match(courseCode);
  if (!match) {
    return {name: label};
  }
  return {code: match[1], name: match[2]};
}

function describe(item: PropSidebarItemCategory, pages: PageLink[]): string {
  if (item.description) {
    return item.description;
  }
  const names = pages
    .filter((page) => page.label !== 'Overview')
    .slice(0, 3)
    .map((page) => page.label);
  if (names.length === 0) {
    return 'Class notes';
  }
  return names.join(' · ');
}

function toCard(item: PropSidebarItem): ClassCard | undefined {
  if (item.type !== 'category' && item.type !== 'link') {
    return undefined;
  }
  const pages = pagesOf(item);
  const href = item.href;
  if (!href || pages.length === 0) {
    return undefined;
  }
  const {code, name} = splitCourse(item.label);
  return {
    href,
    code,
    name,
    description: item.type === 'category' ? describe(item, pages) : name,
    pages,
  };
}

function quickLinks(card: ClassCard): PageLink[] {
  const preferred = quickLinkPreference
    .map((pattern) => card.pages.find((page) => pattern.test(page.label)))
    .filter((page): page is PageLink => page !== undefined);
  if (preferred.length > 0) {
    return preferred;
  }
  return card.pages.filter((page) => page.label !== 'Overview').slice(0, 2);
}

function pageCountLabel(count: number): string {
  return count === 1 ? '1 page' : `${count} pages`;
}

export default function SchoolIndex(): ReactNode {
  const category = useCurrentSidebarCategory();
  const cards = category.items
    .map(toCard)
    .filter((card): card is ClassCard => card !== undefined);
  const latest = cards[cards.length - 1];
  const jumps = latest ? quickLinks(latest) : [];

  return (
    <div className={styles.root}>
      <header className={styles.hero}>
        <div className={styles.glow} aria-hidden="true" />
        <div className={styles.heroBody}>
          <h1 className={styles.title}>School Notes</h1>
          <p className={styles.subtitle}>
            Master's in Computer Science: class notes, journals, and planning.
          </p>
        </div>
      </header>

      {jumps.length > 0 && latest && (
        <nav className={styles.quick} aria-label="Quick links">
          <span className={styles.quickLabel}>
            Quick links
            {latest.code ? <span className={styles.quickCode}>{latest.code}</span> : null}
          </span>
          {jumps.map((page) => (
            <Link key={page.href} className={styles.chip} href={page.href}>
              {page.label}
            </Link>
          ))}
        </nav>
      )}

      {cards.length === 0 ? (
        <p className={styles.empty}>No classes yet.</p>
      ) : (
        <ul className={styles.grid}>
          {cards.map((card) => {
            const topics = card.pages.filter((page) => page.label !== 'Overview').slice(0, 3);
            return (
              <li key={card.href} className={styles.panel}>
                <Link className={styles.panelLink} href={card.href}>
                  {card.code ? <span className={styles.badge}>{card.code}</span> : null}
                  <span className={styles.course}>{card.name}</span>
                  <span className={styles.blurb}>{card.description}</span>
                </Link>
                <div className={styles.meta}>
                  <span className={styles.count}>{pageCountLabel(card.pages.length)}</span>
                  {topics.map((page) => (
                    <Link key={page.href} className={styles.chip} href={page.href}>
                      {page.label}
                    </Link>
                  ))}
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
