"use client";

import { useRouter, useSearchParams } from "next/navigation";
import { useCallback } from "react";

export default function IdNext() {
  const searchParams = useSearchParams()!;
  const id = searchParams.get("id");
  const router = useRouter();

  const createQueryString = useCallback(
    (name: string, value: string) => {
      const params = new URLSearchParams(searchParams);
      params.set(name, value);

      return params.toString();
    },
    [searchParams]
  );

  return (
    <div>
      <button
        onClick={() => {
          let nextId = parseInt(id ?? "0") + 1;
          router.push(`/?${createQueryString("id", nextId.toString())}`);
        }}
        className="bg-gray-200 px-3 py-1 border-gray-200"
      >
        Next Project
      </button>
    </div>
  );
}