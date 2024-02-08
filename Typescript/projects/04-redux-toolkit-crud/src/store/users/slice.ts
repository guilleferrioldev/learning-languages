import { createSlice , type PayloadAction} from "@reduxjs/toolkit"

const DEFAULT_STATE = [
    {
      id: "1",
      name: "Guille Ferriol", 
      email: "guille@gmail.com",
      github: "guilleferrioldev"
    },
    {
      id: "2",
      name: "Leo Doe", 
      email: "loe@gmail.com",
      github: "leo"
    },
    {
      id: "3",
      name: "Midudev", 
      email: "midudev@gmail.com",
      github: "midudev"
    }
  ]

export type UserId = string

export interface User {
    name: string
    email: string
    github: string
}

export interface UserWithID extends User {
    id: UserId
}

const initialState: UserWithID[] = (() => {
    const persistedState = localStorage.getItem("__redux__state__");
    return  persistedState ? JSON.parse(persistedState).users : DEFAULT_STATE;
})(); 

export const usersSlice = createSlice({
    name: 'users', 
    initialState,
    reducers: {
        addNewUser : (state, action:  PayloadAction<User>) => {
            const id = crypto.randomUUID()
            return [...state, {id, ...action.payload}]
        },

        deleteUserById: (state, action: PayloadAction<UserId>) => {
            const id = action.payload;
            return state.filter((user) => user.id !== id)
        }       
    }
})


export default usersSlice.reducer;

export const { deleteUserById , addNewUser} = usersSlice.actions;