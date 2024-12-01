const { readFileAndGetColumns } = require("./utils");

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
