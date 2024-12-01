const { readFileAndGetColumns } = require("./utils");

const calculateTotalSimilarity = ({ left = [], right = [] } = {}) => {
  let totalSimilarity = 0;

  for (let i = 0; i < left.length; i++) {
    const occurrencesInRight = right.filter((n) => n === left[i]);
    const similarity = left[i] * occurrencesInRight.length;

    totalSimilarity += similarity;
  }

  return totalSimilarity;
};

const executeExercise = async () => {
  const { left, right } = await readFileAndGetColumns();

  const totalSimilarity = calculateTotalSimilarity({ left, right });

  console.log({ totalSimilarity });
};

executeExercise();
