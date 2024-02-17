export const cartInitialState = JSON.parse(window.localStorage.getItem('cart')) || []

export const CART_ACTIONS_TYPE = {
    ADD_TO_CART: 'ADD_TO_CART',
    REMOVE_FROM_CART: 'REMOVE_FROM_CART',
    CLEAR_CART: 'CLEAR_CART'
}

export const updateLocalStorage = state => {
  window.localStorage.setItem('cart', JSON.stringify(state))
}

export const cartReducer = (state, action) => {
  const { type: actionType , payload: actionPayload} = action
  
  switch (actionType) {
    case CART_ACTIONS_TYPE.ADD_TO_CART: {
      const productInCartIndex = state.findIndex(item => item.id == actionPayload.id)

      if (productInCartIndex >= 0) {
        const newState = [
          ...state.slice(0, productInCartIndex),
          {
             ...state[productInCartIndex],
              quantity: state[productInCartIndex].quantity + 1 
          },
          ...state.slice(productInCartIndex + 1)
        ]
        updateLocalStorage(newState)
        return newState
      }

      const newState = [
        ...state,
        {
          ...actionPayload,
          quantity: 1
        }
      ]

      updateLocalStorage(newState)
      return newState
    }

    case CART_ACTIONS_TYPE.REMOVE_FROM_CART : {
      const newState =  state.filter(item => item.id !== actionPayload.id)
      updateLocalStorage(newState)
      return newState
    }

    case CART_ACTIONS_TYPE.CLEAR_CART : {
      updateLocalStorage([])
      return []
    }
  }

  return state
}