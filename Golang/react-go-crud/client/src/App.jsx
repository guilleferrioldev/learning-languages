import './App.css'
import { Routes,  Route } from 'react-router-dom'
import Header from "./components/layout/Header";
import Footer from "./components/layout/Footer";

import Home from './pages/Home'
import Blog from './pages/Blog'
import Add from "./pages/Add";
import Edit from "./pages/Edit";

function App () {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blog/:id" element={<Blog />} />
        <Route path="/edit/:id" element={<Edit />} />
        <Route path="/add" element={<Add />} />
      </Routes>
      <Footer />
    </>
  )
}
  
export default App