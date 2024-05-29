import {
    NavLink, 
    Outlet
} from "react-router-dom"

// Outlet charge les composants dans le DOM suivant une route sélectionnées

export default function Root() {

    return (
        <nav>
            <ul>
                <li>
                    <NavLink
                        to={`/`}
                        className="main-router"
                    >
                        Home
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to={`/posts`}
                        className="main-router"
                    >
                        afficher les posts 
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to={`/contact`}
                        className="main-router"
                    >
                        Contact
                    </NavLink>
                </li>
            </ul>
            <Outlet />
        </nav>
    )
}