const fs = require("node:fs/promises");

const readFileAndGetColumns = async () => {
  try {
    const left = [];
    const right = [];

    const data = await fs.readFile("./data.txt", { encoding: "utf8" });
    const rows = data.split("\n")?.filter(Boolean);

    rows.forEach((rowStr) => {
      const [columnA, columnB] = rowStr
        ?.split(/\s+/)
        ?.map((numberStr) => Number.parseInt(numberStr));

      left.push(columnA);
      right.push(columnB);
    });

    return { left, right };
  } catch (err) {
    console.log("Error reading the data file", err);
  }
};

module.exports = { readFileAndGetColumns };
