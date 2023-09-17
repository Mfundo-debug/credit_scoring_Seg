import React, { useState } from 'react';
import axios from 'axios';
import './CreditScoringForm.css';

const CreditScoringForm = () => {
  const [formData, setFormData] = useState({
    // Define form fields here from models.py
    age: '',
    gender: '',
    marital_status: '',
    employment_status: '',
    educational_level: '',
    credit_utilization_ratio: '',
    payment_history: '',
    number_of_credit_accounts: '',
    loan_amount: '',
    interest_rate: '',
    loan_term: '',
    type_of_loan: '',
  });

  const handleChange = (e) => {
    // Handle form input changes and update formData state
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Send formData to your backend API for prediction
    // You'll need to make an API request here
    try {
        const response = await axios.post('/api/predict-credit-score/', formData);
        const prediction = response.data.prediction;
        //Display the prediction to the user or performe some other operation
        console.log('Creidt Score Prediction: ', prediction);
    } catch (err) {
        console.log('Error',err);
    }
  };

  return (
    <div className="credit-form-container">
      <h2>Enter Customer Details</h2>
      <form onSubmit={handleSubmit} className="credit-form">
        <div className="form-group">
          <input type="number" name="age" placeholder="Age" className="form-control" onChange={handleChange} value={formData.age} />
        </div>
        <div className="form-group">
          <input type="text" name="gender" placeholder="Gender" className="form-control" onChange={handleChange} value={formData.gender} />
        </div>
        <div className="form-group">
          <input type="text" name="marital_status" placeholder="Marital Status" className="form-control" onChange={handleChange} value={formData.marital_status} />
        </div>
        <div className="form-group">
          <input type="text" name="employment_status" placeholder="Employment Status" className="form-control" onChange={handleChange} value={formData.employment_status} />
        </div>
        <div className="form-group">
          <input type="text" name="educational_level" placeholder="Educational Level" className="form-control" onChange={handleChange} value={formData.educational_level} />
        </div>
        <div className="form-group">
          <input type="number" name="credit_utilization_ratio" placeholder="Credit Utilization Ratio" className="form-control" onChange={handleChange} value={formData.credit_utilization_ratio} />
        </div>
        <div className="form-group">
          <input type="text" name="payment_history" placeholder="Payment History" className="form-control" onChange={handleChange} value={formData.payment_history} />
        </div>
        <div className="form-group">
          <input type="number" name="number_of_credit_accounts" placeholder="Number of Credit Accounts" className="form-control" onChange={handleChange} value={formData.number_of_credit_accounts} />
        </div>
        <div className="form-group">
          <input type="number" name="loan_amount" placeholder="Loan Amount" className="form-control" onChange={handleChange} value={formData.loan_amount} />
        </div>
        <div className="form-group">
          <input type="number" name="interest_rate" placeholder="Interest Rate" className="form-control" onChange={handleChange} value={formData.interest_rate} />
        </div>
        <div className="form-group">
          <input type="number" name="loan_term" placeholder="Loan Term" className="form-control" onChange={handleChange} value={formData.loan_term} />
        </div>
        <div className="form-group">
          <input type="text" name="type_of_loan" placeholder="Type of Loan" className="form-control" onChange={handleChange} value={formData.type_of_loan} />
        </div>
        <button type="submit" className="btn btn-primary">
          Predict
        </button>
      </form>
    </div>
  );
};

export default CreditScoringForm;
