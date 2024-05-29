import { useGetAllInvoicesQuery } from "../features/invoice"

function Home() {
    // variables définies par défaut dans RTK query
    const { data, error, isLoading } = useGetAllInvoicesQuery()

    return (
        <>
            <h1>Home page API invoices</h1>
            {error ? (
                <>Oh no, there was an error</>
            ) : isLoading ? (
                <>Loading...</>
            ) : data ? (
                <>
                   {data.map(( data, i ) =><p key={i}>{data.trainer}</p>)}
                </>
            ) : null}
        </>
    )
}

export default Home
