import { Products } from "./components/Products"
import { Header } from "./components/Header"
import { Footer } from "./components/Footer"

import { products as initialProducts } from "./mocks/products.json"
import { useState } from "react"
import { useFilters } from "./hooks/useFIlters"
import { IS_DEVELOPMENT } from "./config"

function App () {
    const [ products, setProducts] = useState(initialProducts)
    const { filters, filterProducts, setFilters} = useFilters()
    
    const filteredProducts = filterProducts(products)

    return (
      <>
      <Header changeFilters={setFilters}/>
      <Products products={filteredProducts}/>
      {IS_DEVELOPMENT && <Footer filters={filters}/>}
      </>
      
    )
  }
  
export default App