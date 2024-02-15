import './Products.css'
import { AddCartIcon } from './Icons'
import { useCart} from '../hooks/useCart'

export function Products ({ products }) {
    const { addToCart, cart } = useCart()

    const checkProdcutInCart = product => {
        return cart.some(item => item.id === product.id)
    }

    return ( 
        <main className='products'>
            <ul>
                {products.slice(0,10).map(product => {
                    const isProductInCart = checkProdcutInCart(product)
                    
                    return  (
                    <li key={product.id}>
                        <img src={product.thumbnail} 
                             alt={product.title} 
                        />
                        <div>
                            <strong>{product.title}</strong> - ${product.price}
                        </div>
                        <div>
                            <button onClick={() => addToCart(product)}>
                                <AddCartIcon />
                            </button>
                        </div>
                    </li>
                )})
                }
            </ul>
        </main>
    )
}