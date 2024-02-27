import { Suspense } from "react";
import DataDisplay from "@/app/DataDisplay";
import IdNext from "./id-next";

export default function Home({
  searchParams,
}: {
  searchParams: { id: string | undefined; include: string | undefined };
}) {
  return (
    <div className="mt-10 max-w-7xl px-6 mx-auto">
      <IdNext />
      <div className="mt-10">
        <Suspense key={searchParams.id} fallback={<div>Loading...</div>}>
          <DataDisplay id={searchParams.id} include={searchParams.include} />
        </Suspense>
      </div>
    </div>
  );
}