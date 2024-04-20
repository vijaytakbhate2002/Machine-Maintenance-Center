# Machine Maintenance Center

Welcome to the Machine Maintenance Center project! This application is built using Streamlit and features machine learning models to predict machine failure status based on various parameters. Here's a quick overview of the project:

## Project Overview

- **Objective:** Predictive maintenance for machine failure status using machine learning models.
- **Dataset:** The dataset used contains the following columns:
  - `UID`: Unique identifier ranging from 1 to 10,000.
  - `productID`: Consisting of a letter L, M, or H for low (50% of all products), medium (30%), and high (20%) as product quality variants, and a variant-specific serial number.
  - `air temperature [K]`: Generated using a random walk process later normalized to a standard deviation of 2 K around 300 K.
  - `process temperature [K]`: Generated using a random walk process normalized to a standard deviation of 1 K, added to the air temperature plus 10 K.
  - `rotational speed [rpm]`: Calculated from power of 2860 W, overlaid with normally distributed noise.
  - `torque [Nm]`: Torque values are normally distributed around 40 Nm with a standard deviation of 10 Nm and no negative values.
  - `tool wear [min]`: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process.
  - `machine failure`: Label indicating whether the machine has failed in this particular data point for any of the following failure modes.
  - `target`: Shows whether the machine will fail or not.

## Web Pages

- **Home:** Contains information about the project, developer information, contact details, resume, etc.
- **Single Machine Prediction:** Dedicated for predicting failure status for a single machine; this page will ask for information about the machine and predict whether it will fail in the future or not.
- **Multi Machine Prediction:** Requires a CSV file containing the required columns for prediction. It will return a new CSV file with an added column called predictions. This returned CSV file is downloadable.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/vijaytakbhate2002/Predictive-Machine-Failure-status.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

4. Explore the different web pages and functionalities for predictive maintenance.

## Contributing

We welcome contributions! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
