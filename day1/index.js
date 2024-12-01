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

const calculateTotalDistance = ({ left = [], right = [] } = {}) => {
  const sortedLeft = left.sort();
  const sortedRight = right.sort();

  let totalDistance = 0;

  for (let i = 0; i < sortedLeft.length; i++) {
    const distanceDifference = Math.abs(sortedLeft[i] - sortedRight[i]);

    totalDistance += distanceDifference;
  }

  return totalDistance;
};

const executeExercise = async () => {
  const { left, right } = await readFileAndGetColumns();

  const totalDistance = calculateTotalDistance({ left, right });

  console.log({ totalDistance });
};

executeExercise();
