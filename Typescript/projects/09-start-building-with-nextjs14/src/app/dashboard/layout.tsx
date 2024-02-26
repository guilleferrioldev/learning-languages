export default function DashboardLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>): JSX.Element {
    return (
        <section>
            Esto es el layout del dahsboard
            {children}
        </section>
    )
}