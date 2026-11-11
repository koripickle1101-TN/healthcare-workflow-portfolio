const fs = require('node:fs');
const assert = require('node:assert/strict');
const { JSDOM, VirtualConsole } = require('jsdom');

const html = fs.readFileSync('projects/careflow-intelligence-web/index.html', 'utf8');
const errors = [];
const vc = new VirtualConsole();
vc.on('jsdomError', (error) => errors.push(String(error)));
const dom = new JSDOM(html, {
  url: 'https://careflow.example/',
  runScripts: 'dangerously',
  pretendToBeVisual: true,
  virtualConsole: vc,
  beforeParse(window) {
    window.scrollTo = () => {};
    window.URL.createObjectURL = () => 'blob:demo';
    window.URL.revokeObjectURL = () => {};
  }
});
const { document, Event } = dom.window;
const click = (selector) => {
  const element = document.querySelector(selector);
  assert.ok(element, 'Missing interactive element: ' + selector);
  element.click();
};
const choose = (selector, value) => {
  const element = document.querySelector(selector);
  assert.ok(element, 'Missing filter: ' + selector);
  element.value = value;
  element.dispatchEvent(new Event('change', { bubbles: true }));
};

assert.equal(document.querySelectorAll('.kpi').length, 4, 'Main KPIs must render');
assert.equal(document.querySelectorAll('.mobilebar button').length, 6, 'Six mobile navigation options');
assert.ok(document.body.textContent.includes('Revenue flow.'), 'New editorial hero');
click('.mobilebar button[data-nav="denials"]');
assert.ok(document.body.textContent.includes('Denial Intelligence'), 'Denials view should load');
assert.ok(document.querySelector('[data-cross]'), 'Heatmap must be clickable');
choose('[data-filter="payer"]', 'Payer A');
assert.ok(document.body.textContent.includes('Payer A'), 'Global payer filter should work');
click('tr[data-case]');
assert.ok(document.querySelector('#caseform'), 'Case inspector should open');
choose('[data-filter="caseowner"]', 'Billing');
const form = document.getElementById('caseform');
form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
assert.equal(document.querySelector('#caseform'), null, 'Saved case drawer should close');
assert.ok(dom.window.localStorage.getItem('careflow-demo-notes-v2').includes('Billing'),
          'Demo decision must save locally');
click('.mobilebar button[data-nav="scenario"]');
const slider = document.querySelector('#reduce');
assert.ok(slider, 'Scenario slider must render');
const before = document.querySelector('#scenarioResult').textContent;
slider.value = '75';
slider.dispatchEvent(new Event('input', { bubbles: true }));
const after = document.querySelector('#scenarioResult').textContent;
assert.notEqual(before, after, 'Simulation output must respond to slider');
click('.mobilebar button[data-nav="quality"]');
assert.ok(document.body.textContent.includes('Data Integrity & QA'),
          'Quality audit page must load');
assert.ok(document.body.textContent.includes('Unique claim IDs'),
          'Data audit must show actual validation rules');
assert.deepEqual(errors, [], 'No JS runtime errors');
console.log('PASS: premium UI, 6 nav items, filters, claim inspector, case notes, simulator, quality checks.');
