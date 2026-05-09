import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ProtectedRoute from './components/ProtectedRoute'; 

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header className="App-header">
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>

          {/* All Routes must be inside the Routes component */}
          <Routes>
            <Route
              path="/hr-dashboard"
              element={
                <ProtectedRoute allowedRoles={['hr']}>
                  <h1>HR Dashboard Protected</h1>
                </ProtectedRoute>
              }
            />
            
            {/* Pro-tip: Add a default route so you don't see a blank page at "/" */}
            <Route path="/" element={<div>Home Page</div>} />
          </Routes>
          
        </header>
      </div>
    </BrowserRouter>
  );
}

export default App;