'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'

const links = [
    {
        name: 'Home',
        href: '.'
    },
    {
        name: 'Dashboard',
        href: '/dashboard'
    },
    {
        name: 'Invoices',
        href: '/dashboard/invoices'
    },
    {
        name: 'Customers',
        href: '/dashboard/customers'
    },
]

export default function NavLinks() {
    const pathName = usePathname()
    
    return (
    <>
    {links.map((link) => {
        return <Link
        key={link.name}
        href={link.href}
        className='felx h-[48px] grow items-center justify-center gap-2 bg-gray-50
                  p-3 tex-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none'>
            <p>{link.name}</p>
        </Link>
    })}
    </>
    )
}