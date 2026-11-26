import React, {type ReactNode} from 'react';
import Link from '@docusaurus/Link';
import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/plugin-content-docs/client';
import type {
  PropSidebarItem,
  PropSidebarItemLink,
} from '@docusaurus/plugin-content-docs';

/**
 * Lists the current category's sections from the sidebar, so a new class
 * shows up here without editing this page. A section category links to its
 * own index doc (the overview). That doc is not also a sidebar child, so it
 * is added back as the first card.
 */
function overviewCard(href: string): PropSidebarItemLink {
  return {
    type: 'link',
    href,
    label: 'Overview',
  };
}

function sectionPages(item: PropSidebarItem): PropSidebarItem[] {
  if (item.type !== 'category') {
    return [item];
  }
  const alreadyListed = item.items.some(
    (child) => child.type === 'link' && child.href === item.href,
  );
  return [
    ...(item.href && !alreadyListed ? [overviewCard(item.href)] : []),
    ...item.items,
  ];
}

export default function SchoolSectionCards(): ReactNode {
  const category = useCurrentSidebarCategory();
  const looseDocs = category.items.filter((item) => item.type !== 'category');
  const sections = category.items.filter((item) => item.type === 'category');

  return (
    <>
      {looseDocs.length > 0 && <DocCardList items={looseDocs} />}
      {sections.map((section) => (
        <section key={section.label} className="margin-top--lg">
          <h2>
            {section.type === 'category' && section.href ? (
              <Link href={section.href}>{section.label}</Link>
            ) : (
              section.label
            )}
          </h2>
          <DocCardList items={sectionPages(section)} />
        </section>
      ))}
    </>
  );
}
