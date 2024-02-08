import { type User, SortBy} from '../types.d'

interface Props {
    changeSorting: (sort: SortBy) => void
    deleteUser: (email: string) => void
    showColors: boolean
    users: User[]
}

export function ListOfUsers ({changeSorting, deleteUser, showColors ,users }: Props) {
    return (
        <table width='100%'>
            <thead>
                <tr>
                <th>Photo</th>
                <th className="pointer" onClick={() => changeSorting(SortBy.NAME)}>Name</th>
                <th className="pointer" onClick={() => changeSorting(SortBy.LAST)}>Last Name</th>
                <th className="pointer" onClick={() => changeSorting(SortBy.COUNTRY)}>Country</th>
                <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {
                    users.map((user, index) => {
                        const backgroundColor = index % 2 === 0 ? '#333' : '#555'
                        const color = showColors ? backgroundColor : 'transparent'

                        return (
                            <tr key={user.email} style={{backgroundColor: color}}>
                                <td>
                                    <img src={user.picture.thumbnail}></img>
                                </td>
                                <td>{user.name.first}</td>
                                <td>{user.name.last}</td>
                                <td>{user.location.country}</td>
                                <td>
                                    <button onClick={() => deleteUser(user.email)}>Delete</button>
                                </td>
                            </tr>
                        )
                    })
                }
            </tbody>
        </table>
    )
}