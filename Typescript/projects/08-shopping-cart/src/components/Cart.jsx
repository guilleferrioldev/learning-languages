import { useId } from "react"
import { CartIcon } from "./Icons"
import "./Cart.css"

function CartItem ({ thumbnail, price, title, quantity, addToCart }) {
    return (
      <li>
        <img
          src={thumbnail}
          alt={title}
        />
        <div>
          <strong>{title}</strong> - ${price}
        </div>
  
        <footer>
          <small>
            Qty: {quantity}
          </small>
          <button onClick={addToCart}>+</button>
        </footer>
      </li>
    )
}


export function Cart () {
    const cartChecboxId = useId()

    return (
        <>
        <label className="cart-button" htmlFor={cartChecboxId}>
            <CartIcon />
        </label>
        <input id={cartChecboxId} type="checkbox" hidden/>

        <aside className="cart">
        </aside>
        </>
    )
}