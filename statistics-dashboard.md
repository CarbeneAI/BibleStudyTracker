---
title: "Bible Reading Tracker"
created: 2025-03-15
tags: [dashboard, reading-plan, bible-study]
---

# Bible Reading Tracker

> **Single Source of Truth**: Mark chapters as read in each book file. Progress updates automatically here.

---

## Overall Progress

```dataviewjs
// Get all book files with chapters metadata
const books = dv.pages('"BibleStudyTracker/Old Testament" or "BibleStudyTracker/New Testament"')
    .where(p => p.chapters && p.chapters > 0);

const totalChapters = 1189;
let completedChapters = 0;

books.forEach(book => {
    const done = book.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    completedChapters += done;
});

const pct = ((completedChapters / totalChapters) * 100).toFixed(1);
const barLen = 30;
const filled = Math.round((completedChapters / totalChapters) * barLen);
const bar = '\u2588'.repeat(filled) + '\u2591'.repeat(barLen - filled);

dv.paragraph(`### ${bar} ${pct}%`);
dv.paragraph(`**${completedChapters}** of **${totalChapters}** chapters read`);
```

---

## Testament Progress

```dataviewjs
const books = dv.pages('"BibleStudyTracker/Old Testament" or "BibleStudyTracker/New Testament"')
    .where(p => p.chapters && p.chapters > 0);

const data = {
    'Old Testament': { total: 929, done: 0 },
    'New Testament': { total: 260, done: 0 }
};

books.forEach(book => {
    const testament = book.file.path.includes("Old Testament") ? "Old Testament" : "New Testament";
    data[testament].done += book.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
});

let rows = [];
for (const [name, d] of Object.entries(data)) {
    const pct = ((d.done / d.total) * 100).toFixed(1);
    const barLen = 15;
    const filled = Math.round((d.done / d.total) * barLen);
    const bar = '\u2588'.repeat(filled) + '\u2591'.repeat(barLen - filled);
    rows.push([name, `${d.done}/${d.total}`, `${bar} ${pct}%`]);
}

dv.table(["Testament", "Chapters", "Progress"], rows);
```

---

## Old Testament

### Law (Pentateuch)
```dataviewjs
const books = dv.pages('"BibleStudyTracker/Old Testament/Law"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

### History
```dataviewjs
const books = dv.pages('"BibleStudyTracker/Old Testament/History"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

### Poetry and Wisdom
```dataviewjs
const books = dv.pages('"BibleStudyTracker/Old Testament/Poetry and Wisdom"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

### Major Prophets
```dataviewjs
const books = dv.pages('"BibleStudyTracker/Old Testament/Major Prophets"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

### Minor Prophets
```dataviewjs
const books = dv.pages('"BibleStudyTracker/Old Testament/Minor Prophets"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

---

## New Testament

### Gospels
```dataviewjs
const books = dv.pages('"BibleStudyTracker/New Testament/Gospels"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

### History
```dataviewjs
const books = dv.pages('"BibleStudyTracker/New Testament/History"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

### Pauline Epistles
```dataviewjs
const books = dv.pages('"BibleStudyTracker/New Testament/Pauline Epistles"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

### General Epistles
```dataviewjs
const books = dv.pages('"BibleStudyTracker/New Testament/General Epistles"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

### Prophecy
```dataviewjs
const books = dv.pages('"BibleStudyTracker/New Testament/Prophecy"').where(p => p.chapters > 0).sort(p => p.file.name);
let rows = [];
for (const b of books) {
    const done = b.file.tasks.where(t => t.completed && t.text.includes("Read")).length;
    const pct = Math.round((done / b.chapters) * 100);
    rows.push([b.file.link, `${done}/${b.chapters}`, `${pct}%`]);
}
dv.table(["Book", "Progress", "%"], rows);
```

---

## Recent Reading Activity

```dataviewjs
const books = dv.pages('"BibleStudyTracker/Old Testament" or "BibleStudyTracker/New Testament"')
    .where(p => p.chapters && p.chapters > 0);

let recent = [];

books.forEach(book => {
    book.file.tasks
        .where(t => t.completed && t.text.includes("Read"))
        .forEach(task => {
            const match = task.text.match(/(\d{4}-\d{2}-\d{2})/);
            if (match && !match[1].includes("MM")) {
                recent.push({
                    book: book.file.link,
                    date: match[1]
                });
            }
        });
});

recent.sort((a, b) => b.date.localeCompare(a.date));
recent = recent.slice(0, 10);

if (recent.length > 0) {
    dv.table(["Book", "Date Read"], recent.map(r => [r.book, r.date]));
} else {
    dv.paragraph("*Start reading and marking chapters complete to see activity here.*");
}
```

---

## How to Track Progress

1. **Open any book** from the tables above
2. **Check off chapters** as you read them: `- [x] Read`
3. **Progress updates automatically** on this dashboard

Each book file has checkboxes for every chapter. When you complete a chapter, check it off and your progress will be reflected here.
