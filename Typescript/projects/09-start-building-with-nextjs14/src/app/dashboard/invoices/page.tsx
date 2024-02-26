import { lusitana } from "@/app/ui/fonts";
import { CreateInvoice } from "@/app/ui/invoices/buttons";
import Search from "@/app/ui/search";
import { InvoicesTableSkeleton } from "@/app/ui/skeletons";
import { Suspense } from "react";

export default function InvoicesPage() {
    const query = ""
    const currentPage = 1
    
    return (
        <div className="w-full">
            <div className="flex w-full items-center justify-center">
                <h1 className={`${lusitana.className} text-2xl`}>Invoices</h1>
            </div>
            <div className="mt-4 flex items-center justify-between gap-w md:mt-8">
                <Search placeholder="Search invoices ... "/>
                <CreateInvoice />
            </div>
            <div className="mt-5 flex 2-full justify-center">
                <Suspense key={query + currentPage} fallback={<InvoicesTableSkeleton />}>
                </Suspense>
            </div>
        </div>
    )
}