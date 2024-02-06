import './App.css'
import { Routes,  Route } from 'react-router-dom'
import Home from './pages/Home'
import Blog from './pages/Blog'
import Header from "./components/layout/Header";
import Footer from "./components/layout/Footer";

function App () {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blog/:id" element={<Blog />} />
      </Routes>
      <Footer />
    </>
  )
}
  
export default App