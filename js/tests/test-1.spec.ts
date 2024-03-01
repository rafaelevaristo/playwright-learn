import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {

  await page.goto('https://www.sapo.pt/');
  await page.getByRole('button', { name: 'MAIS OPÇÕES' }).click();
  await page.getByRole('button', { name: 'REJEITAR TODOS' }).click();
  await page.getByRole('button', { name: 'GRAVAR' }).click();
  await page.getByLabel('Menu principal').getByRole('link', { name: 'Economia' }).click();

  await page.close()
});