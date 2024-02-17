import { useReducer } from 'react'
import { cartReducer, cartInitialState, CART_ACTIONS_TYPE} from '../reducers/cart'

export function useCartReducer() {
  const [state, dispatch] = useReducer(cartReducer, cartInitialState)

    const addToCart = product => dispatch({
      type: CART_ACTIONS_TYPE.ADD_TO_CART,
      payload: product
    })

    const removeFromCart = product => dispatch({
      type: CART_ACTIONS_TYPE.REMOVE_FROM_CART,
      payload: product
    })

    const clearCart = () => dispatch({
      type: CART_ACTIONS_TYPE.CLEAR_CART
    })

    return {state, addToCart, removeFromCart, clearCart}
}