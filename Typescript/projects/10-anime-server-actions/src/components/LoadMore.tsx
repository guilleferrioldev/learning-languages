"use client"

import { useInView } from "react-intersection-observer";
import Image from "next/image";
import { useState , useEffect, useRef } from "react";
import { fetchAnime } from "@/app/action";
import AnimeCard from "./AnimeCard";

export type AnimeCard = JSX.Element

export default function LoadMore() {
  const { ref, inView } = useInView();
  const [data, setData] = useState<AnimeCard[]>([])
  const page = useRef(2)

  useEffect(() => {
    if (inView) {
      fetchAnime(page.current, 8)
        .then((res)=> {
          setData([...data, ...res]);
          page.current++;
        })
    }
  }, [inView, data, page])

  return (
    <>
      <section className="grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-10">
        {data}
      </section>

      <section className="flex justify-center items-center w-full">
        <div ref={ref}>
          <Image
            src="./spinner.svg"
            alt="spinner"
            width={56}
            height={56}
            className="object-contain"
          />
        </div>
      </section>
    </>
  );
}