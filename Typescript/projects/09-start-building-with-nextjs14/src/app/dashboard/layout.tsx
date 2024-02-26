import NavLinks from '@/app/ui/dashboard/nav-links';

export default function DashboardLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>): JSX.Element {
    return (
        <section>
            <NavLinks />
            {children}
        </section>
    )
}