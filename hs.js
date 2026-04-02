(() => 
  [...document.querySelectorAll('table.table tbody tr')].map(row => ({
    name: row.querySelector('td.decklist-info a.deck-title').textContent.trim(),
    winrate: parseFloat(row.cells[1].querySelector('span.basic-black-text').textContent),
    pop: parseInt(
      row.cells[2].textContent.match(/\(([\d,]+)\)/)[1].replace(/,/g, '')
    )
  }))
)();
