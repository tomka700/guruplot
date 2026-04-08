(() => 
  [...document.querySelectorAll("table.table tbody tr")].map(row => ({
    name: row.cells[0].textContent.trim(),
    winrate: parseFloat(row.cells[1].textContent),
    pop: parseInt(row.cells[2].textContent.match(/\(([\d,]+)\)/)[1]),
    turns: parseFloat(row.cells[3].textContent),
    duration: parseFloat(row.cells[4].textContent),
    climb_speed: parseFloat(row.cells[5].textContent)
  }))
)();
