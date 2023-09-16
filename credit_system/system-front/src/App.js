import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import CreditScoringForm from "./components/CreditScoringForm";

function App() {
  return (
    <div>
      <Header />
      <main>
      <CreditScoringForm />
      </main>
      <Footer />
    </div>
  );
}
export default App;