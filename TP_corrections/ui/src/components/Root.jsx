import {
    NavLink,
    Outlet
} from "react-router-dom"

// Outlet charge les composants dans le DOM suivant une route sélectionnées

export default function Root() {

    return (
        <nav>
          {/* Définitions des liens cliquables */}
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
                        to={`/invoice`}
                        className="main-router"
                    >
                        Factures
                    </NavLink>
                </li>
            </ul>
            {/* chargement des composants */}
            <Outlet />
        </nav>
    )
}