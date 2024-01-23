const enum ERROR_TYPES {
    NOT_FOUND = 'not found',
    UNAUTHORIZED = 'unauthorized', 
    FORBIDDEN = 'forbidden'
}

function showMessage (error: ERROR_TYPES): void {
    if (error === ERROR_TYPES.NOT_FOUND) {
        console.log("Resource not found")
    }
    else if (error === ERROR_TYPES.UNAUTHORIZED) {
        console.log("You dont have permission to access")
    }
    else if (error === ERROR_TYPES.FORBIDDEN) {
        console.log("You dont have permission to access")
    }
}



