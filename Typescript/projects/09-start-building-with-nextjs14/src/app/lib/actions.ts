'use server'

// Marcar que todas las funciones que se exportan en este archivo son de servidor y por lo tanto no se ejecuta ni se envían al cliente.

import {z} from 'zod'
import {Invoice} from './definitions'
import { sql } from '@vercel/postgres'
import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'

const CreateInvoiceSchema = z.object({
  id: z.string(),
  customerId: z.string(),
  amount: z.coerce.number(),
  status: z.enum(['pending', 'paid']),
  date: z.string()
})

const CreateInvoiceFormSchema = CreateInvoiceSchema.omit({
id: true,
date: true
})

export async function createInvoice(formData: FormData) {
  const {customerId, amount, status} = CreateInvoiceFormSchema.parse({
    customerId: formData.get('customerId'),
    amount: formData.get('amount'),
    status: formData.get('status')
  }) 

  // transformamos para evitar errores de redondeo
  const amountInCents = amount * 100
  // creamos la fecha actual 2023-11-25 <--
  const [date] = new Date().toISOString().split('T')

  console.log({
    customerId,
    amountInCents,
    status,
    date
  })

await sql`
  INSERT INTO invoices (customer_id, amount, status, date)
  VALUES (${customerId}, ${amountInCents}, ${status}, ${date})
`

revalidatePath('/dashboard/invoices')
redirect('/dashboard/invoices')
}