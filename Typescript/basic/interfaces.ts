interface Product {
    id: number
    name: string 
    price: number 
    quantity: number
}

interface Shoe extends Product {
    size: number
}

interface ShoppingCart {
    totalPrice: number 
    products: (Product | Shoe)[]
    add: (product: (Product | Shoe)) => void
}

const shoppingCart: ShoppingCart = {
    totalPrice: 90,
    products: [
        {
            id: 1, 
            name: 'Nike',
            price: 90, 
            quantity: 1, 
            size: 40,
        }
    ],

    add(product: (Product | Shoe)): void {
        console.log(`${product}`)
    }
}

 