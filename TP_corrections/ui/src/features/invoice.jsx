import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const invoiceApi = createApi({
    reducerPath: 'invoiceapi',
    // TODO mettre l'url dans une env ce serait mieux ... 
    baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:8002/' }),
    endpoints: (builder) => ({
        getAllInvoices: builder.query({
            query: () => `api/invoices`,
        }),
    }),
})

export const { useGetAllInvoicesQuery } = invoiceApi